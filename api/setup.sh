#!/bin/bash

# Providing the setup commands for Ubuntu
sudo pip3 install virtualenv
virtualenv env
source env/bin/activate

pip install -r requirements.txt

deactivate