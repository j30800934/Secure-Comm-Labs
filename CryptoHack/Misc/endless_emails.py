#!/usr/bin/env python3
import gmpy2
from itertools import combinations
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

def load_output():
    ret = {'n':[], 'c':[]}
    with open("output_0ef6d6343784e59e2f44f61d2d29896f.txt", 'rb') as fd:
        while True:
            line = fd.readline()
            if not line: break
            line = line.strip().decode()
            if not line: continue
            
            k, v = line.split('=')
            k = k.strip()
            if k == 'e':
                continue
            ret[k].append(int(v))

    return ret

def decrypt(grps, e):
    for grp in combinations(zip(grps['n'], grps['c']), e):
        N = 1
        for x in grp: 
            N *= x[0]

        M = 0
        for x in grp:
            M += x[1] * inverse(N // x[0], x[0]) * (N // x[0])
        M %= N

        # Compute the integer root using gmpy2.iroot and check if it's exact
        m, exact = gmpy2.iroot(M, e)
        if exact:
            print(long_to_bytes(m))

# Reference
# [Hastad’s Broadcast Attack](https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-2/)
grps = load_output()
decrypt(grps, 3)


# This script implements Håstad's Broadcast Attack to break RSA encryption when the same message is broadcasted using different moduli and exponents. It loads RSA public keys and ciphertexts from a file and performs decryption using the Chinese Remainder Theorem (CRT) and integer root extraction. The script computes the product of the moduli (N) and the combined ciphertext (M) using the CRT. It then attempts to find the cubic root of M using gmpy2.iroot, and if the root is exact, it converts the result back to a plaintext message using long_to_bytes.
