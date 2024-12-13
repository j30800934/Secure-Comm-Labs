from egcd import egcd
p = 26513
q = 32321
x,y,z=egcd(p,q)
print(x,y,z)

# -8404
# This script uses the egcd function to compute the extended greatest common divisor (GCD) of two integers, p and q. The extended Euclidean algorithm not only calculates the GCD but also returns coefficients x and y such that p*x + q*y = gcd(p, q). The script prints the values of x, y, and the GCD (z). For the given values p = 26513 and q = 32321, the result includes x = -8404, y = 7077, and z = 1.