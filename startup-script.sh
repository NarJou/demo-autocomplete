#! /bin/bash
sudo apt-get update
sudo apt-get install -y build-essential python-dev libssl-dev libffi-dev git
sudo apt-get install -y python-virtualenv
cd /home/marinenargisse
virtualenv flaskapp

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5
echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.6 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod start

source flaskapp/bin/activate
pip install flask
pip install pymongo

pip install --upgrade pip
pip install fabric