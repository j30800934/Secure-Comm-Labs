#!/usr/bin/env python3
import time
import requests
import string

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

def encrypt(plain):
    url = 'http://aes.cryptohack.org/ctrime/encrypt/'
    rsp = requests.get(url + plain + '/')
    return rsp.json()['ciphertext']

alphabet = '}'+'!'+'_'+'@'+'?'+string.ascii_uppercase+string.digits+string.ascii_lowercase

def bruteforce():
    
    flag = b'crypto{'
    cipher = encrypt(flag.hex())
    mi = len(cipher)

    while True:
        for c in alphabet:
            cipher = encrypt((flag+c.encode()).hex())
            print(c, len(cipher))
            if mi == len(cipher):
                flag += c.encode()
                mi = len(cipher)
                print(mi, flag)
                break
            if c == alphabet[-1]:
                mi += 2
                break
            time.sleep(1)

        if flag.endswith(b'}'): 
            print(flag)
            break

bruteforce()


# This script is attempting to brute-force an AES encryption in CTR (Counter) mode, specifically targeting the decryption of a flag from a cryptography challenge hosted on a website.

# It begins by defining a print_blk function for printing hex blocks in a formatted manner, although it is not actively used in the brute-force process. The encrypt function sends a request to the server with a plaintext value, expecting an AES-encrypted ciphertext in return. The alphabet variable is a custom character set that starts with the character } and includes some special characters, uppercase letters, digits, and lowercase letters. 

# The bruteforce function constructs the flag, starting with crypto{. It then enters an infinite loop, where it tries each character from the alphabet by appending it to the current flag and encrypting it. After each encryption, it compares the length of the resulting ciphertext to the initial length for the crypto{ part. If the lengths are the same, it assumes the character is correct, adds it to the flag, and continues. If the length changes, the process moves to the next possible character. The script uses a time.sleep(1) call to prevent rate-limiting or server throttling.

# Once the script finds the correct flag, it prints it and exits the loop.
