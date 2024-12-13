from Crypto.Util.number import *
from Crypto.Cipher import AES
from pwn import remote
import hashlib
import json


b = 1919572943691512325783103720167834163677411292709378502535498859989993544026380143919501049584589675317643993465536543895780854808442293000014297210200227069779643763121704810281976733978781152126062646602812482025293137787739116693980988513420732289020477701182639042794562638875881378349771734410919106042203493166198706573467903966100368713572415175654342828296086659529676015616513470105470901979846373335352656586302787870238998914215908919919219987614105175

A = 0xde761d0139ca5b6ce2c9dfc9d8ed27d0bae27516def8abf85bea2bf4a0167d5e5efaee006d6c3dcde139503e4837d45c98b1d23f86eee1ce6a2c87197cfdd5300de29ed73330fcac715dff3b9e6848a8941205fb3ab599a3de15bf2b2def976c5ecc351aa572d7f3cb088b5b3f80e2d3d7cc08a728196b668d2a79743e403b42c1232ca0cddd47d4451ca9fbc7640bc1bde18f1f5394512550a619d37ca3560d4b2639d6db9febaea4322615f59907c81f69f6bcf67d29fa82f734d7723c8e05

g = 2
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff

iv = "0ff37c5c8f0340bd17fc195a57d2324c"
enc = "8098fc7fcd3697433d294b2469f0911969c637ef4811489556281f8e88d55282b3d0d9d53fd6d31af46423ac139c48ef"
s = pow(A,b,p)

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def pkcs7_unpad(message, block_size=16):
    if len(message) == 0:
        raise Exception("The input data must contain at least one byte")
    if not is_pkcs7_padded(message):
        return message
    padding_len = message[-1]
    return message[:-padding_len]

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

print(decrypt_flag(s,iv,enc))

# This script connects to a server, extracts Diffie-Hellman parameters, and calculates a shared secret using modular exponentiation. It uses this shared secret to derive an AES key via SHA-1 hashing. Then, it decrypts the provided ciphertext (which is in CBC mode) using the AES key, printing the result after PKCS7 unpadding. The script handles padding verification and decryption correctly to obtain the plaintext.