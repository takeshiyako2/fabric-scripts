from fabric.api import sudo, cd, put
#
# install python3 to CentOS6
#

download_dir = '/usr/local/src'

def setup_yum_repository():
    with cd('/etc/pki/rpm-gpg/'):
        sudo('wget -q http://springdale.math.ias.edu/data/puias/6/x86_64/os/RPM-GPG-KEY-puias')
        sudo('rpm --import RPM-GPG-KEY-puias')
        put('puias-computational.repo', '/etc/yum.repos.d/', use_sudo=True)

def install_by_yum():
    sudo('yum -y install python3.x86_64 python3-devel.x86_64 python3-tools.x86_64')

def version():
    sudo('python3 --version')

def which():
    sudo('which python3')

def install_pip():
    with cd('%s' % download_dir):
        sudo('wget https://pypi.python.org/packages/source/d/distribute/distribute-0.6.49.tar.gz --no-check-certificate')
        sudo('tar xzvf  distribute-0.6.49.tar.gz')
        with cd('distribute-0.6.49'):
            sudo('python3 setup.py install')
            with cd('/usr/lib/python3.3/site-packages/distribute-0.6.49-py3.3.egg'):
                sudo('python3 ./easy_install.py pip')

def pip_version():
    sudo('pip -V')

def modules():
    sudo('python3 -c \"help(\'modules\')\"')

def all():
    '''
setup_yum_repository()
install_by_yum()
version()
which()
install_pip()
pip_version()
modules()
    '''
    exec(all.__doc__.strip())
