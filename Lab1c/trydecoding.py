def hex_to_bytes(hex_string):
    """
    Convert a hex string to bytes.

    Parameters:
    hex_string (str): The hex string to convert.

    Returns:
    bytes: The corresponding byte string.
    """

    return bytes.fromhex(hex_string)

def try_decodings(byte_string):
    """
    Attempt to decode the byte string using various encodings.

    Parameters:
    byte_string (bytes): The byte string to decode.

    Returns:
    dict: A dictionary of results for different encodings.
    """
    encodings = ['utf-8', 'ascii', 'latin-1', 'utf-16']
    results = {}
    
    for encoding in encodings:
        try:
            results[encoding] = byte_string.decode(encoding)
        except (UnicodeDecodeError, TypeError):
            results[encoding] = "Decoding failed"
    
    return results




# Example usage
# Replace this hex string with your actual hex string
hex_string = """
0f351c71e76f5fbe548d4c54a69a2bcb3d2e4ceb3cfb5250c24dff419949683f8ed3a5f04f57116fe797410d2c138b60db6da534a7abe0f658b65b5c0ccbeb67d1c9d9216d8befeb351
73f3596f40d4fa84e1e702818fbc06bec90d4315fceacfa7112c3e55d74aaf3394bb08f7504a8e5019c4e3e838e0f364946f31721a49ad2d24ff6775efcb4f79fe4217a01b43cb5068bf3b52ca76543187274
"""  # Example hex input
byte_string = hex_to_bytes(hex_string)

decoding_results = try_decodings(byte_string)

for enc, result in decoding_results.items():
    print(f"Decoded using {enc}: {result}")
