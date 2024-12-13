from pwn import xor 
from Cryptodome.Util.number import long_to_bytes, bytes_to_long

s = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
t = b"crypto{"

print(xor(s[:7],t)) # b'myXORke'

key = b"myXORkey"
print(xor(s,key))

# b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'
# This script demonstrates the use of the `xor` function from the `pwn` library to perform XOR operations with byte strings. First, it takes a slice of the input string `s` (the first 7 bytes) and XORs it with the string `b"crypto{"`. This results in the key `b"myXORke"`. Then, it XORs the entire string `s` with the key `b"myXORkey"`, revealing the message `b'crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}'`.