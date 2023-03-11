#/bin/bash

#installing python
sudo apt install -y python3
sudo apt install -y python-is-python3
sudo apt install -y python3-pip

#install dependencies
pip install -r requirements.txt

#convert file for a linux enviroment
sudo tr -d '\r' < hashcrack.py > hashcrack_linux.py

#create the binary
sudo chmod +x hashcrack_linux.py
sudo mv hashcrack_linux.py hashcrack
sudo cp  hashcrack /usr/bin

clear

echo "Installation done."

hashcrack --help
