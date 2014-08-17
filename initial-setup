#!/bin/bash

sudo aptitude -y update
sudo aptitude -y upgrade

# install git
sudo apt-get -y install git

# install zsh
sudo apt-get -y install zsh

sudo aptitude -y install build-essential \
                         libsqlite3-dev \
                         libreadline6-dev \
                         libgdbm-dev \
                         zlib1g-dev \
                         libbz2-dev \
                         sqlite3 \
                         tk-dev \
                         zip \
                         python-dev

# install distribute
sudo chmod -R 0775 /usr/local
sudo chgrp -R bpbook /usr/local
wget http://python-distribute.org/distribute_setup.py
sudo python distribute_setup.py

# install pip
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py

# install virtualenv
sudo pip install virtualenv virtualenvwrapper
