#!/bin/sh
#python libraries
sudo -H pip install --upgrade pip
sudo -H pip install --upgrade virtualenv

virtualenv --python=/usr/local/Cellar/python3/3.5.2_3/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
