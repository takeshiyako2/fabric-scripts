#
# install ipafont to CentOS6
#
from fabric.api import env, sudo, task, cd

cache_dir = '/usr/local/src'

@task
def install():
    with cd(cache_dir):
        sudo('wget http://ipafont.ipa.go.jp/ipafont/IPAfont00303.php')
        sudo('unzip IPAfont00303.zip')
        sudo('mkdir /usr/share/fonts/japanese')
        sudo('mkdir /usr/share/fonts/japanese/TrueType')
        sudo('mv IPAfont00303/*.ttf /usr/share/fonts/japanese/TrueType/')
        sudo('wget http://ossipedia.ipa.go.jp/ipafont/ipaexfont/IPAexfont00201.php')
        sudo('unzip IPAexfont00201.zip')
        sudo('mv IPAexfont00201/*.ttf /usr/share/fonts/japanese/TrueType/')
        sudo('fc-cache -fv')

@task
def all():
    '''
# ipafont.all
install()
    '''
    exec(all.__doc__.strip())
