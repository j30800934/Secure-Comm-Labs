from pwn import *
from Crypto.Util.number import *
import random 
import json 

host = 'socket.cryptohack.org'
port = 13426
r = remote(host, port, level='DEBUG')

## public parameters
p = 0x1ed344181da88cae8dc37a08feae447ba3da7f788d271953299e5f093df7aaca987c9f653ed7e43bad576cc5d22290f61f32680736be4144642f8bea6f5bf55ef
q = 0xf69a20c0ed4465746e1bd047f57223dd1ed3fbc46938ca994cf2f849efbd5654c3e4fb29f6bf21dd6abb662e911487b0f9934039b5f20a23217c5f537adfaaf7
g = 2

r.recvuntil(b'I will prove to you that I know flag w such that y = g^w mod p.n')
r.recvline()

e1 = random.randint(0, pow(2, 511))
challenge = {
    "e": e1
}
payload = json.dumps(challenge).encode()
r.sendline(payload)

response = json.loads(r.recvline().strip().decode())
z1 = response["z"]

r.recvline()

e2 = e1 + 1
challenge = {
    "e": e2
}
payload = json.dumps(challenge).encode()
r.sendline(payload)

response = json.loads(r.recvline().strip().decode())
z2 = response["z2"]

print(long_to_bytes(z2 - z1))

r.interactive()

## crypto{specially_sound_sigmas}

# The code implements a Sigma protocol to prove knowledge of a secret w such that  y = g^w mod p  without revealing w itself. The participant starts by sending a random challenge e1 to the server. The server responds with a value z1. The participant then sends a second challenge e2, calculated as e1 + 1, and receives the second response z2. The difference between z2 and z1 is calculated and converted to bytes, which reveals the flag "crypto{specially_sound_sigmas}".