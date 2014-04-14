#
# install jstat2gf to CentOS6
#
from fabric.api import env, sudo, task, cd

cache_dir = '/usr/local/src'

@task
def install():
    sudo('yum -y install git libyaml-devel *YAML*')
    sudo('curl -L http://cpanmin.us | perl - --sudo App::cpanminus')
    sudo('/usr/local/bin/cpanm --version')
    sudo('ln -s /usr/local/bin/cpanm /usr/bin/cpanm')
    with cd(cache_dir):
         sudo('git clone https://github.com/kazeburo/jstat2gf.git')
         with cd('jstat2gf'):
             sudo('cpanm --installdeps .')
@task
def help():
    sudo('perl %s/jstat2gf/jstat2gf.pl --help' % cache_dir)

@task
def all():
    '''
# jstat2gf.all
install()
    '''
    exec(all.__doc__.strip())
