# #!/usr/bin/env python3
# import requests

# def encrypt():
#     url = "http://aes.cryptohack.org/bean_counter/encrypt/"
#     rsp = requests.get(url)
#     return rsp.json()['encrypted']

# png_hdr = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])
# encrypted = bytes.fromhex(encrypt())

# keystream = []
# for i in range(len(png_hdr)):
#     keystream.append(png_hdr[i] ^ encrypted[i])

# print(keystream)

# png = [0]*len(encrypted)
# for i in range(len(encrypted)):
#     png[i] = encrypted[i] ^ keystream[i%len(keystream)]

# with open('bean_counter.png', 'wb') as fd:
#     fd.write(bytes(png))



#!/usr/bin/env python3
import requests

def encrypt():
    url = "http://aes.cryptohack.org/bean_counter/encrypt/"
    rsp = requests.get(url)
    return rsp.json()['encrypted']

# PNG header bytes
png_hdr = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])

# Get the encrypted data from the server
encrypted = bytes.fromhex(encrypt())

# Calculate the keystream by XOR'ing the header with the encrypted data
keystream = []
for i in range(len(png_hdr)):
    keystream.append(png_hdr[i] ^ encrypted[i])

# Decrypt the encrypted data by XOR'ing it with the keystream
png = [0] * len(encrypted)
for i in range(len(encrypted)):
    png[i] = encrypted[i] ^ keystream[i % len(keystream)]

# Write the decrypted data to a PNG file
with open('bean_counter.png', 'wb') as fd:
    fd.write(bytes(png))

print("Decrypted image written to 'bean_counter.png'")
