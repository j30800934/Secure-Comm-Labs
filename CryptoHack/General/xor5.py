from PIL.Image import open, fromarray
from numpy import array
img1 = array(open(r"D:\ctfs\crypto\CryptoHack_Solutions\General\Xor\flag.png"))
img2 = array(open(r"D:\ctfs\crypto\CryptoHack_Solutions\General\Xor\lemur.png"))
fromarray(img1^img2).show()

## crypto{X0Rly_n0t!}
# This script uses the `PIL` (Python Imaging Library) to open two image files, `flag.png` and `lemur.png`, and converts them into NumPy arrays. It then performs a bitwise XOR operation between the two image arrays (`img1^img2`) and creates a new image from the result using `fromarray()`. The resulting image is displayed, and it represents the flag `crypto{X0Rly_n0t!}`.