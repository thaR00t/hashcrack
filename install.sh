#/bin/bash

#installing python
sudo apt install -y python3
sudo apt install -y python-is-python3
sudo apt install -y python3-pip

#install dependencies
pip install -r requirements.txt

#convert file for a linux enviroment
tr -d '\r' < hashcrack.py > hashcrack_linux.py

#create the binary
chmod +x hashcrack_linux.py
mv hashcrack_linux.py hashcrack
sudo cp  hashcrack /usr/bin

echo "Installation done."

hashcrack --help

