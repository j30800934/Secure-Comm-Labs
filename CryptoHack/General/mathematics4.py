from math import gcd
print(gcd(273246787654,65537))

# since gcd = 1, thus answer by fermat's little theorem is 1
# This script uses Python's `gcd` function from the `math` module to calculate the greatest common divisor (GCD) of `273246787654` and `65537`. Since the GCD is `1`, the result implies that the two numbers are coprime. According to Fermat's Little Theorem, if two numbers are coprime, the answer to certain modular exponentiation problems involving them will be `1`.