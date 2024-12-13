from pwn import *
from Crypto.Util.number import *
r = remote('socket.cryptohack.org', 13374)
print(r.recvline())
r.sendline(b'{"option": "get_secret"}')
x = eval(r.recvline().decode().strip('\n'))["secret"]
print(x)
print(b'{"option": "sign", "msg": \"' + str(x).encode() + b'\"}')
r.sendline(b'{"option": "sign", "msg": \"' + str(x).encode() + b'\"}')
x = int(eval(r.recvline().decode().strip('\n'))["signature"][2:],16)
print(long_to_bytes(x))

# crypto{d0n7_516n_ju57_4ny7h1n6}

# This code connects to a remote server and sends a request to fetch a secret message. It receives the secret, then uses that secret as a message to sign, sending it back to the server. The server returns a signature, which the code converts from hexadecimal and prints the corresponding bytes. The message retrieved is "crypto{d0n7_516n_ju57_4ny7h1n6}".