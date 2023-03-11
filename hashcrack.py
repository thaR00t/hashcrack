#!/usr/bin/python3

import hashlib
import binascii
import argparse
from rich import print
from datetime import datetime
import textwrap

try:

    def hash_md5():
        #open wordlist
        with open(wordlist_location, 'r') as f:
            #analyze all line in the wordlist
            for line in f.readlines():
                #find the word which corrispond with the hash
                hash_ob = hashlib.md5(line.strip().encode())

                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input:
                    print(f'Your clear text hash is: [bold green][[/bold green] [bold white]{line.strip()}[/bold white] [bold red]][/bold red]')
                    exit(0)
    def hash_sha1():
        with open(wordlist_location, 'r') as s:
            #analyze all line in the wordlist
            for line in s.readlines():
                #find the word which corrispond with the hash
                hash_ob = hashlib.sha1(line.strip().encode())
                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input:
                    print(f'Your clear text hash is: [bold green][[/bold green] [bold white]{line.strip()}[/bold white] [bold red]][/bold red]')
                    exit(0)
    def hash_sha224():
        with open(wordlist_location, 'r') as f:
            #analyze all line in the wordlist
            for line in f.readlines():
                #find the word which corrispond with the hash
                hash_ob = hashlib.sha224(line.strip().encode())

                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input:
                    print(f'Your clear text hash is: [bold green][[/bold green] [bold white]{line.strip()}[/bold white] [bold red]][/bold red]')
                    exit(0)
    def hash_sha256():
        with open(wordlist_location, 'r') as f:
            for line in f.readlines():
                hash_ob = hashlib.sha256(line.strip().encode())
                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input:
                    print(f'Your clear text hash is: [bold green][[/bold green] [bold white]{line.strip()}[/bold white] [bold red]][/bold red]')
                    exit(0)
    def hash_sha512():
        with open(wordlist_location, 'r') as f:
            for line in f.readlines():
                hash_ob = hashlib.sha512(line.strip().encode())
                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input:
                    print(f'Your clear text hash is: [bold green][[/bold green] [bold white]{line.strip()}[/bold white] [bold red]][/bold red]')
                    exit(0)
    def hash_sha384():
        with open(wordlist_location, 'r') as f:
            for line in f.readlines():
                hash_ob = hashlib.sha384(line.strip().encode())
                hashed_pass = hash_ob.hexdigest()
                if hashed_pass == hash_input:  
                    print(f'Your clear text hash is: [bold green][[/bold green] [bold white]{line.strip()}[/bold white] [bold red]][/bold red]')
                    exit(0)

    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="Hash cracker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""AVAILABLE HASH(md5 is by default):
AVAILABLE HASH:
    [*] md5
    [*] sha1    
    [*] sha224
    [*] sha256
    [*] sha384
    [*] sha512
MD5 HASH Usage: python hashcrack.py -w <wordlist> -m md5 <hash>
SHA1 HASH Usage: python hashcrack.py -w <wordlist> -m sha1 <hash>
SHA224 HASH Usage: python hashcrack.py -w <wordlist> -m sha224 <hash>
SHA384 HASH Usage: python hashcrack.py -w <wordlist> -m sha384 <hash>
SHA512 HASH Usage: python hashcrack.py -w <wordlist> -m 512 <hash>
"""))
        parser.add_argument("hash",help="Hash to crack")
        parser.add_argument('-w','--wordlist', help="wordlist to crack your hash")
        parser.add_argument('-m','--mode', default="md5",help="Select a type of hash (md5 is the deafult one so you don't need to specify it)")
        args = parser.parse_args()
        wordlist_location = args.wordlist
        hash_input = args.hash
        mode = args.mode
        
    t = datetime.now()
    ft = t.strftime("%H:%M:%S")
    print("""[bold green]
     _               _                         _    
    | |__   __ _ ___| |__   ___ _ __ __ _  ___| | __
    | '_ \ / _` / __| '_ \ / __| '__/ _` |/ __| |/ /    [/bold green]
    [bold white]| | | | (_| \__ \ | | | (__| | | (_| | (__|   < [/bold white]
    [bold red]|_| |_|\__,_|___/_| |_|\___|_|  \__,_|\___|_|\_\ [/bold red]
""")

    print('-'*50)
    print(f"[!]Hash: {hash_input}")
    print(f"[!]Mode: {mode}")
    print(f"[!]Using wordlist: {wordlist_location}")
    print(f"[!]Cracking started at {ft}")
    print("-"*50)
    if mode == "sha1":
        hash_sha1()
    elif mode == "md5":
        hash_md5()
    elif mode == "sha224":
        hash_sha224()
    elif mode == "sha256":
        hash_sha256()
    elif mode == "sha384":
        hash_sha384()
    elif mode == "sha512":
        hash_sha512()
    
    else:
        print(f"Sorry but I can't decrypt this hash type [bold red][ {mode} ][/bold red] :(")
#except TypeError:
#    print("Missing wordlist")
except KeyboardInterrupt:
    print("\nScript interrupted by user.")
