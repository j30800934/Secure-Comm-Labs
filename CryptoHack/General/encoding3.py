import base64
s = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print(base64.b64encode(bytes.fromhex(s)))

# crypto/Base+64+Encoding+is+Web+Safe/
# This script converts a hexadecimal string to bytes using bytes.fromhex(), encodes the bytes to a Base64 string using base64.b64encode(), and prints the result. The output represents the Base64-encoded string crypto/Base+64+Encoding+is+Web+Safe/.