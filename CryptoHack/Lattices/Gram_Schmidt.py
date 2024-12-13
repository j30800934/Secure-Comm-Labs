v1 = [4,1,3,-1]
v2 = [2,1,-3,4]
v3 = [1,0,-2,7]
v4 = [6,2,9,-5]
basis = []
basis.append(v1)
basis.append(v2)
basis.append(v3)
basis.append(v4)

def dot_product(a,b,n):
    sum = 0
    for i in range(n):
        sum+=(a[i]*b[i])
    return sum
def scalar_multiplication(k,a,n):
    for i in range(n):
        a[i]=k*a[i]
    return a 
def subtraction(a,b,n):
    list2 = []
    for i in range(n):
        list2.append(a[i]-b[i])
    return list2

def gram_schmidt(b,k,n):
    list2 = []
    list2.append(b[0])
    for i in range(1,k):
        x = b[i]
        for j in list2:
            x = subtraction(x,scalar_multiplication(dot_product(b[i],j,n)/dot_product(j,j,n),j,n),n)
        list2.append(x)
    return list2 

print(gram_schmidt(basis,4,4))

# [[8.592592592592592, 2.148148148148148, 6.444444444444444, -2.148148148148148], [-2.1517865472525424, -0.9529340423546974, 2.121046739434649, -3.1969400130609205], [-0.07888707939423852, -0.11132148834378605, 0.21961943009058033, 0.231988484351001], [-0.3619189659458108, 0.9161073825503355, 0.2148893860303271, 0.11309967685806738]]

# This script performs the Gram-Schmidt orthogonalization process on a set of 4 vectors (`v1`, `v2`, `v3`, and `v4`). The function `dot_product` computes the dot product of two vectors, `scalar_multiplication` multiplies a vector by a scalar, and `subtraction` subtracts one vector from another. The core of the script lies in the `gram_schmidt` function, which orthogonalizes the input basis by iterating over the vectors and subtracting projections onto the previously processed vectors. The result is a set of orthogonalized vectors, which is printed as the output.