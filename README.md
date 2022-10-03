# Hashcrack

This is a tool to crack MD5 and SHA hashes, it works on Linux and Windows too.

Note: If you are using this tool on windows make sure that the wordlist is in the current directory of the file.
If you are on linux, you don't have any kind of problem.

Installation:
```
pip install -r requirements.txt
```
![2022-10-02-23-59-45](https://user-images.githubusercontent.com/87804260/193478208-04d179ed-1868-4898-b32b-c5a3ead17fd8.gif)

Usage
---
MD5 Hash

```
python hashcrack.py -w <wordlist> -m md5 <hash>
```

SHA1 Hash


```
python hashcrack.py -w <wordlist> -m sha1 <hash>
```

SHA224 Hash

```
python hashcrack.py -w <wordlist> -m sha224 <hash>
```

SHA256


```
python hashcrack.py -w <wordlist> -m sha256 <hash>
```

SHA384

```
python hashcrack.py -w <wordlist> -m sha384 <hash>
```

SHA512

```
python hashcrack.py -w <wordlist> -m sha512 <hash>
```
