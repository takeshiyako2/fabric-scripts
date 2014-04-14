# What's this?

As first, you have to setup Fabric(http://fabfile.org/) on your PC.  
And then, use this scripts.  

## Usage

Clone this repository.
```
$ git clone git@github.com:takeshiyako2/fabric-scripts.git
$ cd fabric-scripts
```

### Install Python3

It's a install script for Python3 and PIP on CentOS6.  

```
$ fab -H 192.168.1.0 -f centos6-python3.py all
```



### Apache Thrift

It's a install script for Apache Thrift(http://thrift.apache.org/) on CentOS6. 
```
$ fab -H 192.168.1.0 -f centos6-thrift.py all
```

