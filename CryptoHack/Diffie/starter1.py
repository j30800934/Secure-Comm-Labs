def binexp(x, y, z):
    if (y==0):
        return 1%z
    ans = binexp(x, y//2, z)
    ans = ((ans%z)*(ans%z))%z
    if (y%2):
        ans = (ans*x)%z 
    return ans 
p = 991
g = 209
print(binexp(g,p-2,p))

# 569

# This script implements binary exponentiation to efficiently compute gp−2mod  pgp−2modp, which is used to calculate the modular inverse of g modulo p. The function binexp(x, y, z) recursively calculates xymod  zxymodz using the method of exponentiation by squaring, and the final result prints 569, which is gp−2mod  pgp−2modp.
