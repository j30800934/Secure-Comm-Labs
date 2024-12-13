from Cryptodome.Util.number import *

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
print((p-1)*(q-1))

# This code calculates the value of(p-1) x (q-1), wherep andq are large prime numbers. This is typically used in RSA encryption to compute the totient ofn = p x q. The result is857504083339712752489993810776 x 1029224947942998075080348647218.