#
# install Thrift to CentOS6
#
from fabric.api import task, sudo, cd
from fabric.contrib import files

download_dir = '/usr/local/src'
version = '0.9.1'
source_url = 'http://ftp.kddilabs.jp/infosystems/apache/thrift/%s/thrift-%s.tar.gz' % (version, version)

@task
def install_yum():
    sudo('yum -y install automake libtool flex bison pkgconfig gcc-c++ boost-devel libevent-devel zlib-devel python-devel ruby-devel')

@task
def install():
    with cd(download_dir):
        sudo('wget %s -O thrift-%s.tar.gz' % (source_url, version))
        sudo('tar vzxf thrift-%s.tar.gz' % version)
        with cd('thrift-%s' % version):
            sudo('./configure --with-cpp=no')
            sudo('make')
            sudo('make install')
            sudo('ln -s /usr/local/bin/thrift /usr/bin/thrift')

@task
def all():
    '''
# thrift.all
install_yum()
install()
    '''
    exec(all.__doc__.strip())
