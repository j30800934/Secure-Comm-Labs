def hex_to_bytes(hex_string):
    """
    Convert a hexadecimal string to bytes.

    Parameters:
    hex_string (str): The hexadecimal string to convert.

    Returns:
    bytes: The corresponding bytes representation of the hex string.
    """
    try:
        # Remove any whitespace and convert hex to bytes
        return bytes.fromhex(hex_string.strip())
    except ValueError as e:
        print(f"Error converting hex to bytes: {e}")
        return None

# Example usage:
hex_string = """
127d183cb07342a042d40553e9cc3dd83d2e5cea3be91756cf46f904d74f6c3fbcd3b8f04f
431c27af8842003147c27a9425b82fe2e6f8ed5fb2540e05c9ee23d681cc3d28c7f6e2275
22466c2fe555aa34f116d7b1fb58168f4d8d72c0dd3b3bb701197fe087baefe784eac9c30
02b4f9488f0029c08606341d49ef113ff7cdd8c60abe6f5cefbff792e9317e4f9d36b948dfdd
f409e264580f65
"""
result = hex_to_bytes(hex_string)

if result is not None:
    print(f"Bytes: {result}")
