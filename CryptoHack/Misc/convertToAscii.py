import base64
from Crypto.Util.number import *
# from Crypto.Util.number import long_to_bytes

def convertB64(texts):
    # Convert hex string to bytes, then decode to a UTF-8 string
    text = bytes.fromhex(texts)
    # Encode the string in base64
    res = base64.b64encode(text)  # Encode the string back to bytes
    return res.decode('utf-8')  # Return the base64 string

# Hexadecimal string to convert
hex_text = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

# Call the function and print the result
myb64 = convertB64(hex_text)
# print(myb64)

# crypto/Base+64+Encoding+is+Web+Safe/



def convertAscii(numbers):
    ascii_chars = []  # Create an empty list to store the ASCII characters
    for number in numbers:
        ascii_chars.append(chr(number))  # Convert each number to its ASCII character
    return ascii_chars  # Return the list of ASCII characters

# flag = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag = [99, 114, 121, 112, 116, 111, 123, 89, 111, 117, 95, 119, 105, 108, 108, 95, 98, 101, 95, 119, 111, 114, 107, 105, 110, 103, 95, 119, 105, 116, 104, 95, 104, 101, 120, 95, 115, 116, 114, 105, 110, 103, 115, 95, 97, 95, 108, 111, 116, 125]

# result = convertAscii(flag)

# print(result)

# ['c', 'r', 'y', 'p', 't', 'o', '{', 'Y', 'o', 'u', '_', 'w', 'i', 'l', 'l', '_', 'b', 'e', '_', 'w', 'o', 'r', 'k', 'i', 'n', 'g', '_', 'w', 'i', 't', 'h', '_', 'h', 'e', 'x', '_', 's', 't', 'r', 'i', 'n', 'g', 's', '_', 'a', '_', 'l', 'o', 't', '}']
# def convertToOrd(texts):
#     text_array = []
#     for text in texts:
#         text_array.append(ord(text))
#     return text_array

# # text = [c, r, y, p, t, o, {, A, S, C, I, I, _, p, r, 1, n, t, 4, b, l, 3, }]
# text =[63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d]

# res = convertToOrd(text.toString)

# print(res)

def convertToOrd(texts):
    ord_array = []  # List to store the ordinal values
    for text in texts:
        ord_array.append(ord(text))  # Convert each character to its ordinal value
    return ord_array

# Given hexadecimal string (note: should be converted to bytes first)
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert hex string to bytes and then to characters
text = bytes.fromhex(hex_string).decode('utf-8')  # Convert hex to string

# Get the ordinal values
res = convertToOrd(text)  # Call the function with the converted text

# print(res)  # Print the result




def convertToMsg(large_integer):

    # Convert the integer back to bytes
    message_bytes = long_to_bytes(large_integer)

    # Decode the bytes to get the original message
    message = message_bytes.decode('utf-8')

    return message


# Given base-10 integer
large_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

result = convertToMsg(large_integer)

# print(result);


def xor_string_with_13(label):
    # Initialize an empty string to store the XORed result
    result = ''
    
    # Loop through each character in the string
    for char in label:
        # XOR the Unicode value of the character with 13
        xor_char = chr(ord(char) ^ 13)
        # Append the resulting character to the result string
        result += xor_char
    
    # Return the flag with the XORed string
    return f"crypto{{{result}}}"

# Example usage
label = "label" 
flag = xor_string_with_13(label)
print(flag)
