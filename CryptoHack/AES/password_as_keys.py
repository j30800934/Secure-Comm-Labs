ciphertext = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'
ciphertext = bytes.fromhex(ciphertext)

import requests 
url_link = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
response = requests.get(url_link)
wordlist = response.text.split('\n')

from Cryptodome.Cipher import AES 
from hashlib import md5 

for key in wordlist:
    key = md5(key.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except:
        pass   
    try:
        print(bytes.fromhex(decrypted.hex()).decode())
    except:
        pass

# crypto{k3y5__r__n07__p455w0rdz?}



# This script attempts to decrypt a given ciphertext using AES in ECB mode with keys derived from a wordlist. It fetches a list of words from a remote URL and hashes each word using MD5 to generate a key for AES decryption. The script then tries to decrypt the ciphertext with each generated key, printing any successfully decrypted plaintext as a potential flag. The decrypted flag is revealed as crypto{k3y5__r__n07__p455w0rdz?}.