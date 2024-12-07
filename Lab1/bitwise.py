def bitwise_xor(a,b,op):
    
    result = None

    if op == 'or':
        result = a | b
    elif op == 'and':
        result = a & b
    elif op == 'xor':
        result = a ^ b
    else:
        raise ValueError("Invalid operation. Use 'or', 'and', or 'xor'.")
    
    return result


q1 = bitwise_xor(0x43, 0x21, 'or')
q2 = bitwise_xor(0x43, 0x21, 'and')  
q3 = bitwise_xor(0x43, 0x21, 'xor')  

print(q1)
print(q2)
print(q3)

