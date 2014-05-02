# -*- coding: utf-8 -*-

from fabric.api import env, put, sudo, settings, cd, run, local, task
from fabric.contrib import project
import os, glob

download_dir = '/usr/local/src'
luajit_version = '2.0.3'
nginx_version = '1.6.0'

@task
def install_luajit():
    sudo('yum install -y curl tar make gcc')
    with cd(download_dir):
        sudo('curl -O http://luajit.org/download/LuaJIT-%s.tar.gz' % luajit_version)
        sudo('tar xf LuaJIT-%s.tar.gz' % luajit_version)
        with cd('LuaJIT-%s' % luajit_version):
            sudo('make')
            sudo('make PREFIX=/usr/local/luajit install')

@task
def install_nginx_with_lua_nginx_module():
    sudo('yum install -y git curl tar bzip2 make gcc-c++ zlib-devel')
    with cd(download_dir):
        sudo('git clone git://github.com/simpl/ngx_devel_kit.git')
        sudo('git clone git://github.com/chaoslawful/lua-nginx-module.git')
        sudo('curl -LO http://downloads.sourceforge.net/project/pcre/pcre/8.34/pcre-8.34.tar.bz2')
        sudo('tar xf pcre-8.34.tar.bz2')
        sudo('curl -O http://nginx.org/download/nginx-%s.tar.gz' % nginx_version)
        sudo('tar xf nginx-%s.tar.gz' % nginx_version)
        with cd('nginx-%s' % nginx_version):
            sudo(
'export LUAJIT_LIB=/usr/local/luajit/lib &&'
'export LUAJIT_INC=/usr/local/luajit/include/luajit-2.0 &&'
'./configure --prefix=/usr/local/nginx '
'--pid-path=/var/run/nginx.pid '
'--sbin-path=/usr/sbin/nginx '
'--conf-path=/etc/nginx/nginx.conf '
'--error-log-path=/var/log/nginx/error.log '
'--http-log-path=/var/log/nginx/access.log '
'--with-pcre=/usr/local/src/pcre-8.34 '
'--add-module=/usr/local/src/ngx_devel_kit '
'--add-module=/usr/local/src/lua-nginx-module '
'--with-http_realip_module '
'--with-http_stub_status_module '
'--with-ld-opt="-Wl,-rpath,$LUAJIT_LIB" && make && make install')
    sudo('nginx -V')

@task
def all():
    '''
# nginx_lua.all
install_luajit()
install_nginx_with_lua_nginx_module()
    '''
    exec(all.__doc__.strip())
