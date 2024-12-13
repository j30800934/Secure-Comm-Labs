from sage.all import *
from Cryptodome.Util.number import *
## set up elliptic curve parameters
p = 9739
E = EllipticCurve(Zmod(p),[497,1768])
## define the points and perform point addition
P = E(493, 5564)
Q = E(1539, 4742)
R1 = E(4403,5202)

print(P+P+Q+R1)
# crypto{4215,2162}

# The script sets up an elliptic curve over the finite field GF(9739) with the curve equation \( y^2 = x^3 + 497x + 1768 \). It defines three points \( P \), \( Q \), and \( R1 \) on the curve and performs elliptic curve point addition to compute the sum \( P + P + Q + R1 \). The result is printed, which is expected to be a point on the curve, corresponding to the solution "crypto{4215,2162}".