from Cryptodome.Util.number import *
from pwn import xor 

s = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
s = bytes.fromhex(s)
for i in range(256):
    ans = xor(s,i)
    if b'crypto' in ans:
        print(ans)

# crypto{0x10_15_my_f4v0ur173_by7e}
# This script attempts to decrypt a hexadecimal-encoded string by applying a bitwise XOR operation with each possible byte value (ranging from 0 to 255). It uses the `xor` function from the `pwn` library to perform the XOR operation. After each XOR, the script checks if the resulting byte string contains the substring `b'crypto'`. Once it finds a match, it prints the decrypted result, which is `crypto{0x10_15_my_f4v0ur173_by7e}`.