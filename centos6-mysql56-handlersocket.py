from fabric.api import sudo, settings, task, cd, put

cache_dir = '/usr/local/src'
version = 'mysql-5.6.17'
source_url = 'http://dev.mysql.com/get/Downloads/MySQL-5.6/%s.tar.gz' % version

@task
def install_yum():
    sudo('yum -y install wget cmake libtool libtool-ltdl libtool-ltdl-devel libedit-devel')

@task
def mysql_user():
    with settings(warn_only=True):
        sudo('groupadd mysql')
        sudo('useradd -g mysql mysql')

@task
def mysql_get_source():
    sudo('wget %s -O %s/%s.tar.gz' % (source_url, cache_dir, version))

@task
def mysql_untar():
    with cd(cache_dir):
        sudo('tar xf %s.tar.gz' % version)

@task
def mysql_install():
    with cd('%s/%s' % (cache_dir, version)):
        sudo('cmake . -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_UNIX_ADDR=/var/lib/mysql/mysql.sock')
        sudo('make')
        sudo('make install')

@task
def mysql_setup():
    with cd('/usr/local/mysql'):
        sudo('chown -R mysql .')
        sudo('chgrp -R mysql .')
        sudo('scripts/mysql_install_db --user=mysql --datadir=/var/lib/mysql -basedir=/usr/local/mysql')
        sudo('chown -R root .')
        sudo('chown -R mysql data')
        sudo('cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld')
        sudo('ln -s /usr/local/mysql/bin/mysql /usr/bin/mysql')

@task
def chmod_mysql_dir():
    sudo('chmod 755 /var/lib/mysql')

@task
def mysql_restart():
    sudo('/etc/init.d/mysqld restart')
    sudo('tail -500 /var/lib/mysql/mysqld-error.log')
    sudo('pgrep -f -l mysql')

@task 
def handlersocket_get_source():
    with cd(cache_dir):
        sudo('git clone git://github.com/DeNA/HandlerSocket-Plugin-for-MySQL.git')

@task
def handlersocket_install():
    with cd('%s/HandlerSocket-Plugin-for-MySQL' % cache_dir):
        sudo('./autogen.sh')
        sudo('./configure --with-mysql-source=/usr/local/src/mysql-5.6.15 --with-mysql-bindir=/usr/local/mysql/bin --with-mysql-plugindir=/usr/local/mysql/lib/plugin')
        sudo('make')
        sudo('make install')

@task
def show_plugins():
    sudo('mysql -uroot -e "show plugins;"')

@task
def info():
    print('\n\nU can login to mysql by\n$ mysql -u root\n')

@task
def all():
    '''
# mysql_handlersocket.all
install_yum()
mysql_user()
mysql_get_source()
mysql_untar()
mysql_install()
mysql_setup()
chmod_mysql_dir()
handlersocket_get_source()
handlersocket_install()
mysql_restart()
show_plugins()
info()
    '''
    exec(all.__doc__.strip())


@task
def mysql_put_production_conf():
    put('templates/mysql_handlersocket/production.cnf', '/etc/my.cnf', use_sudo=True)

