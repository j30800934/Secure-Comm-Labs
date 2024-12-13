from Cryptodome.Util.number import *

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi_n = (p-1)*(q-1)

print(pow(e,-1,phi_n))

# This code calculates the modular inverse of e modulo phi(n) , where e is the public exponent and phi(n) is the totient of n , with n = p x q . The result is the private exponent d used in RSA encryption, ensuring that e x d equiv 1 pmod{phi(n)} .

