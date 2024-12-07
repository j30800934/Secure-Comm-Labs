def decode_bytes_to_plaintext(byte_string):
    """
    Convert a byte string to plaintext, attempting to decode it as UTF-8 or ASCII.
    Handles errors gracefully and prints the output.

    Parameters:
    byte_string (bytes): The byte string to decode.

    Returns:
    str: The decoded plaintext or an indication of failure.
    """
    try:
        # Attempt to decode directly to UTF-8
        decoded_string = byte_string.decode('utf-8')
        return decoded_string
    except UnicodeDecodeError:
        # If decoding fails, return an indication of failure
        return "Decoding failed. The byte string may not represent valid UTF-8 text."

# Example usage
byte_string = b'\x0f8\x1a9\xfeoA\xbdW\xc4FF\xea\xcc>\xcb+iZ\xe7)\xee\x17J\xc6P\xab\x0c\x92Tzs\xb1\x9c\xa7\xa2M@\x16+\xea\x9c\r\x1c,\x13\x95g\x8fm\xec*\xe8\xb4\xea\xa4I\xb1Q\x15\x07\xc3\xe0m\xd6\xc9\xc0,i\xc5\xec\xa4$\x1d?5\x85\xf4D@\xad\x01\x10x8\x1b\xac\xc0u\xe4\xc3'

# Call the function and print the result
plaintext = decode_bytes_to_plaintext(byte_string)
print("Plaintext:", plaintext)
