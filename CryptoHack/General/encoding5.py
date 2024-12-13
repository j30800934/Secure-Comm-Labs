from Cryptodome.Util.number import long_to_bytes, bytes_to_long
from pwn import *
import json
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(100):
    received = json_recv()
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    if received["type"] == "base64":
        encoded = base64.b64decode(received["encoded"]).decode('utf-8')
    elif received["type"] == "hex":
        encoded = bytes.fromhex(received["encoded"]).decode('utf-8')
    elif received["type"] == "rot13":
        encoded = codecs.encode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
        encoded = bytes.fromhex(received["encoded"][2:]).decode('utf-8')
    elif received["type"] == "utf-8":
        encoded = ""
        for b in received["encoded"]:
            encoded += chr(b)
    to_send = {
        "decoded": encoded
    }
    json_send(to_send)
res = r.recv()
print(res)

# crypto{3nc0d3_d3c0d3_3nc0d3}
# This script connects to a remote server using the pwn library and processes a series of encoding challenges. It establishes a connection to socket.cryptohack.org on port 13377 and exchanges data in JSON format. For each challenge, the script receives a message containing an encoded value and its type. Depending on the type, it decodes the value using the appropriate method: Base64 decoding for base64, hexadecimal conversion for hex, ROT13 transformation for rot13, conversion from a hexadecimal big integer for bigint, and UTF-8 character conversion for utf-8. After decoding the value, the script sends the decoded result back to the server in JSON format. This process repeats for up to 100 challenges, ultimately receiving the final response, which includes the flag crypto{3nc0d3_d3c0d3_3nc0d3}.