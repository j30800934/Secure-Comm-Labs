#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))


# This script checks if the Python version is 2 and prints a warning if so. It then processes a list of integers (`ords`), applying a XOR operation with the value `0x32` to each integer and converting the result into a character. The characters are concatenated to form the flag, which is then printed.
