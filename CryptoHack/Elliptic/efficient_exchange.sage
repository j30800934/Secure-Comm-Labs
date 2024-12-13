from sage.all import *
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import hashlib

E = EllipticCurve(GF(9739),[497,1768])
q_x = 4726
Qx = E(q_x,mod(q_x**3 + 497*q_x + 1768,9739).sqrt())
nB = 6534

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16)
    else:
        return plaintext

shared_secret = (nB*(Qx))[0]
iv = "cd9da9f1c60925922377ea952afc212c"
ciphertext = "febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"

print(decrypt_flag(shared_secret, iv, ciphertext))
# crypto{3ff1c1ent_k3y_3xch4ng3}

#  This script performs elliptic curve cryptography (ECC) on a curve defined by a=497a=497, b=1768b=1768, and p=9739p=9739 to calculate a shared secret using a point QQ. It then uses this shared secret to derive an AES encryption key via SHA-1 hashing. The script decrypts a ciphertext that has been encrypted with AES in CBC mode, using the shared secret-derived key and a provided initialization vector (IV). If the ciphertext is padded using PKCS7, the padding is removed, and the decrypted flag is printed.