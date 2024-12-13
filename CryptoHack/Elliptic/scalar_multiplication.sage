from sage.all import *
from Cryptodome.Util.number import *
## set up the elliptic curve parameters
p = 9739
E = EllipticCurve(Zmod(p),[497,1768])
## perform scalar multiplication
P = E(2339, 2213)
print(7863*P)

# crypto{9467,2742}

# This Sage code defines an elliptic curve \( y^2 = x^3 + 497x + 1768 \mod 9739 \) and performs scalar multiplication. It multiplies the point \( P = (2339, 2213) \) by the scalar \( 7863 \), then prints the resulting point. The result is \( (9467, 2742) \), which is the answer in the format `crypto{9467,2742}`.