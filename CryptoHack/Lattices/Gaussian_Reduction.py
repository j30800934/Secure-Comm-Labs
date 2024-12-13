def dot_product(a,b,n):
    sum = 0
    for i in range(n):
        sum+=(a[i]*b[i])
    return sum

def Lattice_Reduction(u,v):
    if dot_product(v,v,len(v))<dot_product(u,u,len(u)):
            t = u 
            u = v 
            v = t
    m = dot_product(u,v,len(u))//dot_product(u,u,len(u))
    while m!=0: 
        if dot_product(v,v,len(v))<dot_product(u,u,len(u)):
            t = u 
            u = v 
            v = t
        m = dot_product(u,v,len(u))//dot_product(u,u,len(u))
        if (m==0):
            break
        for i in range(len(v)):
            v[i] = v[i] - m*u[i]
    return u,v

u = [87502093, 123094980]
v = [846835985, 9834798552]
x,y = Lattice_Reduction(u,v)
print(dot_product(x,y,len(x)))

## 7410790865146821

# This script implements a lattice reduction algorithm and calculates the dot product of two vectors, `x` and `y`, after reducing them. The function `dot_product` computes the sum of element-wise products of two lists. The `Lattice_Reduction` function modifies the vectors `u` and `v` by reducing them through a series of steps, including swapping and updating the vectors based on their dot products. The final step prints the dot product of the reduced vectors `x` and `y`, which results in `7410790865146821`.
