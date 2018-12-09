#!/usr/bin/env bash

echo "-------------------------------------"
echo "*** Verifying python installation ***"
if command -v python &>/dev/null; then
    echo Python is installed
else
    OS="`uname`"
    case $OS in
      'Darwin')
        OS='Mac'
        brew install python
        ;;
      'Linux')
        OS='Linux'
#       TODO:
#       by running `uname -a` we can distinguish between Debian/Ubuntu and RedHat/CentOS
#       and after that use either apt-get or yum utility
#       on Ubuntu python is installed by default
#       on Debian:
#         sudo apt-get install python
#       on RedHat / CentOS:
#         sudo yum install python
        ;;
      'WindowsNT')
        OS='Windows'
        # installing python 2.7.3
        mkdir -p ~/local
        curl -OL http://www.python.org/ftp/python/2.7.3/Python-2.7.3.tgz
        tar xvzf Python-2.7.3.tgz
        cd Python-2.7.3
        ./configure
        make
        make altinstall prefix=~/local  # specify local installation directory
        ln -s ~/local/bin/python2.7 ~/local/bin/python
        cd ..
        ;;
      *) ;;
    esac
fi