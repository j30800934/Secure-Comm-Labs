from sage.all import *
from Cryptodome.Util.number import *
from hashlib import sha1
## setup elliptic curve parameters
E = EllipticCurve(GF(9739),[497,1768])
QA = E(815, 3190)
nB = 1829
print(sha1(str((nB*QA)[0]).encode()).hexdigest()) 
# crypto{80e5212754a824d3a4aed185ace4f9cac0f908bf}


# This script uses SageMath to set up an elliptic curve defined over a finite field \( GF(9739) \), with specific parameters \( a = 497 \) and \( b = 1768 \). It multiplies a point \( QA = (815, 3190) \) by a scalar \( nB = 1829 \), then computes the SHA-1 hash of the x-coordinate of the resulting point and prints it in hexadecimal format. The output matches a flag format, suggesting the result is the flag.