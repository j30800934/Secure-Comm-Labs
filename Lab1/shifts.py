import sys

def shifts(val):
    try:
        # If command-line arguments are provided, use them
        if len(sys.argv) > 1:
            val = sys.argv[1]
        
        # Print the binary input
        print("Binary form:  \t\t", val)

        # Convert binary to decimal
        dec = int(val, 2)
        print("Decimal form:  \t\t", dec, "\t", bin(dec)[2:].rjust(8, '0'))

        # Perform shifts and print results
        res = (dec << 1) & 0xff  # Left shift by 1
        print("Shift left  (1):\t", res, "\t", bin(res)[2:].rjust(8, '0'))

        res = (dec << 2) & 0xff  # Left shift by 2
        print("Shift left  (2):\t", res, "\t", bin(res)[2:].rjust(8, '0'))

        res = (dec >> 1) & 0xff  # Right shift by 1
        print("Shift right (1):\t", res, "\t", bin(res)[2:].rjust(8, '0'))

        res = (dec >> 2) & 0xff  # Right shift by 2
        print("Shift right (2):\t", res, "\t", bin(res)[2:].rjust(8, '0'))

    except ValueError as ve:
        print(f"Error: Invalid binary input '{val}'. Please ensure it's a valid binary string.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Default value if no command-line argument is provided
val = "101001"  # Binary for 'A' (65 in decimal)

# Call the function
shifts(val)


# def shifty(val):
#     try:
#         # Convert the input to binary if it's not already in binary format
#         if not val.startswith('0b'):
#             if val.isdigit():
#                 # Assume it's a decimal number
#                 dec = int(val)
#             elif val.startswith('0x'):
#                 # Assume it's a hexadecimal number
#                 dec = int(val, 16)
#             elif val.startswith('0o'):
#                 # Assume it's an octal number
#                 dec = int(val, 8)
#             else:
#                 raise ValueError("Invalid input format. Please provide a binary, decimal, hex, or octal value.")
#         else:
#             # Input is already in binary
#             dec = int(val, 2)

#         # Convert the decimal value to binary
#         binary_str = bin(dec)[2:].rjust(8, '0')

#         print("Binary form:  \t\t", binary_str)
#         print("Decimal form:  \t\t", dec, "\t", binary_str)

#         # Perform shifts and print results
#         res = (dec << 1) & 0xff  # Left shift by 1
#         print("Shift left  (1):\t", res, "\t", bin(res)[2:].rjust(8, '0'))

#         res = (dec << 2) & 0xff  # Left shift by 2
#         print("Shift left  (2):\t", res, "\t", bin(res)[2:].rjust(8, '0'))

#         res = (dec >> 1) & 0xff  # Right shift by 1
#         print("Shift right (1):\t", res, "\t", bin(res)[2:].rjust(8, '0'))

#         res = (dec >> 2) & 0xff  # Right shift by 2
#         print("Shift right (2):\t", res, "\t", bin(res)[2:].rjust(8, '0'))

#     except ValueError as ve:
#         print(f"Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Default value if no command-line argument is provided
# val = 41 # "01000001"  # Binary for 'A' (65 in decimal)

# # If a command-line argument is provided, use it instead of the default
# if len(sys.argv) > 1:
#     val = sys.argv[1]

# # Call the function
# shifty(val)

