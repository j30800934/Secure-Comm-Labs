from sage.all import *

E = EllipticCurve(GF(163), [145, 49])
print(E.j_invariant())

## 127

# This script uses SageMath to define an elliptic curve over the finite field \( \mathbb{F}_{163} \) with the equation \( y^2 = x^3 + 145x + 49 \). It then calculates and prints the \( j \)-invariant of the curve. The \( j \)-invariant is a value that uniquely characterizes an elliptic curve over a field, and for this particular curve, the output is `127`.