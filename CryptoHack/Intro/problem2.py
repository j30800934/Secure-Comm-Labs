#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))

# crypto{z3n_0f_pyth0n}

# This script checks if the Python version is 2 and prints a message if so. It then processes a list of integers `ords` by applying a bitwise XOR operation with `0x32` (50 in decimal) to each element. The result is converted to characters using `chr()`, and the characters are concatenated to form the flag, which is `crypto{z3n_0f_pyth0n}`.