from Cryptodome.Util.number import *

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi_n = (p-1)*(q-1)

print(pow(e,-1,phi_n))

