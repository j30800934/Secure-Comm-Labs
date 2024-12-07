import string
import random
from base64 import b64encode, b64decode

# Step 1: Read the content from intercepted.txt
with open('intercepted.txt', 'r') as file:
    secret = file.read().strip()  # Removes any leading/trailing whitespace or newlines

secret_encoding = ['step1', 'step2', 'step3']

def step1(s):
    _step1 = str.maketrans(
        "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA",
        "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON"
    )
    return s.translate(_step1)

def step2(s):
    return b64encode(s.encode('utf-8')).decode('utf-8')

def step3(plaintext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = str.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

def make_secret(plain, count):
    a = '2{}'.format(b64encode(plain.encode('utf-8')).decode('utf-8'))
    for _ in range(count):
        r = random.choice(secret_encoding)
        si = secret_encoding.index(r) + 1
        _a = globals()[r](a)
        a = '{}{}'.format(si, _a)
    return a

if __name__ == '__main__':
    # Example count value; replace with the correct value if needed
    print(make_secret(secret, count=3))
