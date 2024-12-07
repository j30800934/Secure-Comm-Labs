def filter_readable_chars(decoded_string):
    """
    Filter the decoded string to only include readable characters.

    Parameters:
    decoded_string (str): The decoded string to filter.

    Returns:
    str: A string containing only readable characters.
    """
    return ''.join(filter(lambda x: x.isprintable(), decoded_string))

# Assuming 'decoded' contains the output from the Latin-1 decoding
decoded_latin1 = """
89þoA½WÄFFêÌ>Ë+iZç)îJÆP«
,gmì*è´ê¤I±QÃàmÖÉÀ,iÅì¤$?5                     Tzs±§¢M@+ê
ôD@­x8ÀuäÃ
"""
filtered_output = filter_readable_chars(decoded_latin1)

print("Filtered Readable Characters:", filtered_output)
