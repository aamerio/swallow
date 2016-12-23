# python libraries
sudo pip install --upgrade pip
#sudo pip install --upgrade zlib
sudo pip install --upgrade virtualenv

virtualenv --python=/Library/Frameworks/Python.framework/Versions/3.6/bin/python venv
source venv/bin/activate
pip install -r requirements.txt
