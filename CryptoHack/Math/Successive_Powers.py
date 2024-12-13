from Cryptodome.Util.number import *
flag = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
for i in range(852,1000):
    if not isPrime(i):
        continue
    e=True
    x = (pow(flag[0],-1,i)*flag[1])%i
    for j in range(1,11):
        if (pow(flag[j],-1,i)*flag[j+1])%i!=x:
            e=False
            break
    if e:
        print(i,x)
    else:
        continue

# crypto{919,209}

# This script checks for primes between 852 and 1000 and calculates a modular inverse operation using values from the flag list. It verifies if a certain condition holds for each prime and prints the prime and corresponding result if the condition is met. The output is crypto{919,209}.
