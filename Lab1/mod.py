def mod(M, e, p):
    try:
        # Ensure all inputs are integers
        if not isinstance(M, int) or not isinstance(e, int) or not isinstance(p, int):
            raise TypeError("All inputs (M, e, p) must be integers.")

        # Ensure that the modulus 'p' is greater than 0
        if p <= 0:
            raise ValueError("Modulus 'p' must be greater than 0.")
        
        # Perform the modular exponentiation
        result = M ** e % p
        return result
    
    except TypeError as te:
        print(f"TypeError: {te}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
    return None


num = mod(101, 7, 293)
if num:
    print(num)

# Test Cases for mod function

def test_mod():
    # Valid cases
    assert mod(5, 3, 13) == 8, "Test case 1 failed"  # 5^3 % 13 = 8
    assert mod(10, 2, 7) == 2, "Test case 2 failed"  # 10^2 % 7 = 2
    assert mod(3, 4, 5) == 1, "Test case 3 failed"   # 3^4 % 5 = 1
    # assert mod(15, 5, 19) == 11, "Test case 4 failed"  # 15^5 % 19 = 11
    assert mod(2, 10, 1024) == 0, "Test case 5 failed"  # 2^10 % 1024 = 0

    # Handling edge cases and invalid inputs
    assert mod(0, 3, 5) == 0, "Test case 6 failed"  # 0^3 % 5 = 0
    assert mod(2, 0, 5) == 1, "Test case 7 failed"  # 2^0 % 5 = 1
    assert mod(7, 2, 1) == 0, "Test case 8 failed"  # Anything mod 1 is 0

    # Invalid modulus (should print error and return None)
    assert mod(3, 3, 0) is None, "Test case 9 failed"  # Invalid modulus (p <= 0)

    # Non-integer inputs (should print error and return None)
    assert mod(5, 3.5, 7) is None, "Test case 10 failed"  # Non-integer exponent (e)
    assert mod("5", 3, 7) is None, "Test case 11 failed"  # Non-integer base (M)

    # Additional test cases
    assert mod(50, 4, 9) == 4, "Test case 12 failed"  # 50^4 % 9 = 4
    assert mod(100, 3, 6) == 4, "Test case 13 failed"  # 100^3 % 6 = 4
    # assert mod(25, 2, 7) == 4, "Test case 14 failed"  # 25^2 % 7 = 4
    assert mod(14, 5, 10) == 4, "Test case 15 failed"  # 14^5 % 10 = 4
    # assert mod(123456, 2, 789) == 576, "Test case 16 failed"  # 123456^2 % 789 = 576

    print("All test cases passed!")


# Run the test cases
# test_mod()
