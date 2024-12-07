def equivalent(type, val):

    result = "Dec"
    if type == "Bin":
        result = bin(val)
    elif type == "Hex":
        result = hex(val)
    elif type == "Oct":
        result = oct(val)
    elif type == "Dec":
        result = val
    elif type == "Char":
        result = chr(val)
    else:
        raise ValueError("Invalid type. Use 'Bin', 'Hex', 'Dec', 'Oct', or 'Char'.")

    return result



value = equivalent("Dec", '93')
print(value)
