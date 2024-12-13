p = 28151
def binexp(x, y, z):
    if (y==0):
        return 1%z
    ans = binexp(x, y//2, z)
    ans = ((ans%z)*(ans%z))%z
    if (y%2):
        ans = (ans*x)%z 
    return ans 
for i in range(2,p):
    ans = 0
    if (binexp(i,2,p)>1):
        ans+=1
    if (binexp(i,5,p)>1):
        ans+=1
    if (binexp(i,10,p)>1):
        ans+=1
    if (binexp(i,25,p)>1):
        ans+=1
    if (binexp(i,50,p)>1):
        ans+=1
    if (binexp(i,2*563,p)>1):
        ans+=1
    if (binexp(i,5*563,p)>1):
        ans+=1
    if (binexp(i,10*563,p)>1):
        ans+=1
    if (binexp(i,25*563,p)>1):
        ans+=1
    if (binexp(i,1,p)>1):
        ans+=1
    if (binexp(i,563,p)>1):
        ans+=1
    if (ans==11):
        print(i)
        break
# primitive_element = 7


# This script finds the primitive root of a prime number `p` by testing candidate numbers from 2 to \( p-1 \). For each candidate \( i \), it checks if the powers of \( i \) modulo \( p \) (specifically powers \( 2, 5, 10, 25, 50, 2*563, 5*563, 10*563, 25*563, 1, 563 \)) are greater than 1. If all 11 conditions hold true, the number \( i \) is printed as the primitive root of `p`. The script identifies `7` as the primitive root.