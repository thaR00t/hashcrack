#!/usr/bin/env python
import os
from os import system
from sys import platform



def check_root():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

if __name__ == '__main__':
    if platform == "linux" or platform == "linux2":
            check_root()
            system("apt install python3")
            system("apt install python-is-python3")
            system("pip install -r requirements.txt")
            system("tr -d '\r' < hashcrack.py > hashcrack.py")
            system("chmod +x hashcrack_linux.py")
            system("mv hashcrack_linux.py hashcrack")
            system("cp hashcrack /usr/bin")
            print("done.")
    if platform == "windows":
        print("This script only works on Linux.\nYou can run: python hashcrack.py")


