def euc_gcd(a,b):
    if b==0:
        return a
    else:
        return euc_gcd(b,a%b)
a = 66528
b = 52920
print(euc_gcd(a,b))

# 1512

# This script implements the Euclidean algorithm to compute the greatest common divisor (GCD) of two integers, a and b. It recursively calculates the GCD by repeatedly taking the remainder until b becomes zero. The GCD of 66528 and 52920 is printed as 1512.