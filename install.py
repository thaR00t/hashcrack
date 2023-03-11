#!/usr/bin/env python
import os
from os import system

def check_root():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")


if __name__ == '__main__':
    check_root()
    system("pip install -r requirements.txt")
    system("chmod +x hashcrack.py")
    system("mv hashcrack.py hashcrack")
    system("cp hashcrack /usr/bin")
    print("done.")

