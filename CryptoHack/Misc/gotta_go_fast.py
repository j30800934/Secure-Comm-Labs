from Crypto.Util.number import *
from pwn import *
import hashlib 
import time

def generate_key():
    current_time = int(time.time())
    key = long_to_bytes(current_time)
    return hashlib.sha256(key).digest()

def encrypt(b,key):
    assert len(b) <= len(key), "Data package too large to encrypt"
    ciphertext = b''
    for i in range(len(b)):
        print(b[i], key[i], b[i]^key[i])
    for i in range(len(b)):
        ciphertext += bytes([b[i] ^ key[i]])
    return ciphertext.hex()

x = hashlib.sha256(long_to_bytes(int(time.time())+1)).digest()

r = remote('socket.cryptohack.org', 13372, level = 'DEBUG')
r.recv()

r.sendline(b'{\"option\": \"get_flag\"}')
param = eval(r.recvline().strip(b'\n').decode())
print(param["encrypted_flag"])    
enc_flag = long_to_bytes(int(param["encrypted_flag"],16))
print(long_to_bytes(int(encrypt(enc_flag,x),16)))


# This script uses a time-based key generation approach for encryption, where the key is derived from the current timestamp and hashed with SHA-256. It encrypts the given data by XORing each byte of the input with the corresponding byte from the key. It connects to a remote server using the pwn library, retrieves an encrypted flag, and attempts to decrypt it using the generated key. However, there's a small bug in the encrypt() function: the ciphertext is being converted to hex but not returned correctly. Additionally, the flag decryption might not work as expected due to potential issues with timing or key generation.

