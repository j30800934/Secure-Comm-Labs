from pwn import *
host, port='socket.cryptohack.org', 11112
r = remote(host,port)

res = (r.recv())
r.sendline(b'{"buy":"flag"}')
rem = (r.recvline())
print(rem)
r.close()

# b'{"flag": "crypto{sh0pp1ng_f0r_fl4g5}"}\n'

# This script connects to the remote server at `socket.cryptohack.org` on port `11112` using the `pwn` library. It first receives a response from the server, then sends a JSON-encoded string `{"buy":"flag"}` as a request to purchase the flag. After sending the request, it waits for the server's response, which is expected to be a JSON object containing the flag. The script prints the response, which contains the flag `crypto{sh0pp1ng_f0r_fl4g5}`.
