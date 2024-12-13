from Cryptodome.Util.number import *
from pwn import xor
import requests

url_enc = "https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
url_dec = "https://aes.cryptohack.org/ecbcbcwtf/decrypt/"

def encrypt():
    return eval(requests.get(url_enc).text)["ciphertext"]
def get_encrypt():
    ciphertext = encrypt()
    iv = long_to_bytes(int(ciphertext[:32],16))
    cipher = long_to_bytes(int(ciphertext[32:],16))
    ciphertexts = [cipher[i:i+16].hex() for i in range(0,len(cipher),16)]
    return iv,ciphertexts
def decrypt(ciphertext):
    url = url_dec + ciphertext + "/"
    return eval(requests.get(url).text)["plaintext"]
iv, ciphertexts = get_encrypt()
data_array = []
flag = b''
previous = ""
for data in ciphertexts:
    if len(flag)==0:
        data_array.append(decrypt(data))
        previous=data
        flag += xor(iv,long_to_bytes(int(data_array[len(data_array)-1],16)))
    else:
        data_array.append(decrypt(data))
        flag += xor(bytes.fromhex(previous),bytes.fromhex(data_array[len(data_array)-1]))
        previous=data
print(flag)


# This script decrypts an encrypted flag using the ECB and CBC modes of AES encryption. It retrieves encrypted data from a server, processes it to extract the IV and ciphertext blocks, and then decrypts them block by block. The decryption uses the CBC property that each plaintext block is the XOR of the decrypted ciphertext and the previous ciphertext (or IV for the first block). The final output reconstructs the flag in plaintext.