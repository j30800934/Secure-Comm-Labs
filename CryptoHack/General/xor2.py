from Cryptodome.Util.number import *
KEY1 = bytes_to_long(bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"))
KEY12 = bytes_to_long(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"))
KEY23 = bytes_to_long(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"))
FKEY123 = bytes_to_long(bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))
flag = FKEY123^KEY1^KEY23
print(long_to_bytes(flag))

# crypto{x0r_i5_ass0c1at1v3}
# This script performs a bitwise XOR operation on three given keys (`KEY1`, `KEY23`, and `FKEY123`) and computes the flag. The hexadecimal values of `KEY1`, `KEY12`, `KEY23`, and `FKEY123` are first converted to long integers using `bytes_to_long()`. Then, it calculates `flag` by applying the XOR operation: `FKEY123 ^ KEY1 ^ KEY23`. Finally, it converts the resulting value back into bytes and prints the flag, which is `crypto{x0r_i5_ass0c1at1v3}`.