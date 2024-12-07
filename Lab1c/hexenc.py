def hex_to_ascii(hex_string):
    try:
        # Remove any spaces or newlines
        hex_string = hex_string.replace('\n', '').replace(' ', '')
        
        # Convert hex to bytes
        bytes_data = bytes.fromhex(hex_string)
        
        # Convert bytes to ASCII
        ascii_string = bytes_data.decode('ascii', errors='ignore')  # 'ignore' ignores invalid ASCII bytes
        
        return ascii_string
    except ValueError as ve:
        print(f"Error: Invalid hex string. {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example hex string
hex_string = """
0f351c71c7654ff251de056ea68920cf2d7d49e53ff9174bd303fc04d74e7e69ad9cb9bf561
60c2aea960d002b139b6b8f25982fe2e6e9f158a2451944c3f623d19dc425648beceb621f
38768abb4f47ad46176b7b04b3c069a0c4da3b0dd3bea96a54b7e4453989f86b55ba8b6
35b90f944
"""

# Convert to ASCII
ascii_output = hex_to_ascii(hex_string)

print("ASCII Output:")
print(ascii_output)
