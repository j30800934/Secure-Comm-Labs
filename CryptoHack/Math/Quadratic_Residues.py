p = 29
ints = [14, 6, 11]
for i in ints:
    print(pow(i,(p-1)//2,p),end=" ")
qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"\nflag{ {min(qr)}}")

# flag{8}

# This script calculates the quadratic residues modulo 29 for the integers in the list `ints`, prints the results of modular exponentiation, and then finds the smallest value in the set of quadratic residues that match the given list. The output is `flag{8}`.