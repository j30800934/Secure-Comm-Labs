v = [4,6,2,5]

def dot_product(a,b,n):
    sum = 0
    for i in range(n):
        sum+=(a[i]*b[i])
    return sum
from math import sqrt
print(sqrt(dot_product(v,v,4)))

# This script calculates the Euclidean norm (or length) of the vector `v` by computing the square root of the dot product of `v` with itself. The dot product is calculated by multiplying corresponding elements of the vector `v` and summing the results. Then, the square root of this sum gives the norm of the vector `v`. The output of `print(sqrt(dot_product(v,v,4)))` will be the Euclidean norm of the vector `[4, 6, 2, 5]`.