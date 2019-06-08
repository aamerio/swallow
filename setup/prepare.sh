#!/bin/sh
#python libraries
sudo -H pip3 install --upgrade pip
sudo -H pip3 install --upgrade virtualenv

virtualenv --python=/usr/local/Cellar/python3/3.6.0/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
