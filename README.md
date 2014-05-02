# What's this?

There are Fabric script collection for some middleware for CentOS6. 

## Usage

As first, you have to setup Fabric(http://fabfile.org/) on your PC.
And then, use these scripts.

Clone this repository.
```
$ git clone git@github.com:takeshiyako2/fabric-scripts.git
$ cd fabric-scripts
```

### Python3

It's a install script for Python3 and PIP on CentOS6.  

```
$ fab -H 192.168.1.0 -f centos6-python3.py all
```



### Apache Thrift

It's a install script for Apache Thrift(http://thrift.apache.org/). 
```
$ fab -H 192.168.1.0 -f centos6-thrift.py all
```

### jstat2gf

It's a install script for jstat2gf(https://github.com/kazeburo/jstat2gf).  


```
$ fab -H 192.168.1.0 -f centos6-jstat2gf.py all
```


### MySQL5.6 and HandlerSocket

It's a install script for MySQL5.6 and HandlerSocket(https://github.com/DeNA/HandlerSocket-Plugin-for-MySQL).  

```
$ fab -H 192.168.1.0 -f centos6-mysql56-handlersocket.py all
```


### Nginx with HttpLuaModule

It's a install script for Nginx whtih HttpLuaModule(http://wiki.nginx.org/HttpLuaModule).

```
$ fab -H 192.168.1.0 -f centos6-nginx_lua.py all
```


