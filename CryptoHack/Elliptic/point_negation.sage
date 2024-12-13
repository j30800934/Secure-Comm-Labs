from sage.all import *
from Cryptodome.Util.number import *
## set up elliptic curve parameters
p = 9739
E = EllipticCurve(Zmod(p),[497,1768])
## perform point negation
P = E(8045,6936)
print(-P)

# crypto{8045,2803}

# In the Sage code, you're performing point negation on an elliptic curve. When you negate a point on the curve, you flip the sign of the yy-coordinate while keeping the xx-coordinate the same.

Given that P=(8045,6936)P=(8045,6936), negating this point will result in −P=(8045,−6936mod  9739)−P=(8045,−6936mod9739).