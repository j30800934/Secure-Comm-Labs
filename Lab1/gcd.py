def gcd(a, b):
    # Error handling for invalid inputs
    try:
        # Ensure that both inputs are integers
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both a and b must be integers.")

        # Ensure that both inputs are positive integers
        if a < 0 or b < 0:
            raise ValueError("Both a and b must be non-negative integers.")
        
        # Apply the Euclidean algorithm to find GCD
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        
        return a

    except TypeError as te:
        print(f"TypeError: {te}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
g = gcd(5432, 634)
if g:
    print(f"GCD: {g}")
