def linear_congruential_generator(a, seed, c, m, count=10):
    """Generate a sequence using the Linear Congruential Generator (LCG) formula."""
    try:
        # Ensure all inputs are integers and the modulus is greater than 0
        if not all(isinstance(x, int) for x in [a, seed, c, m]):
            raise TypeError("All inputs must be integers.")
        if m <= 0:
            raise ValueError("Modulus 'm' must be greater than 0.")
        
        # Initialize the sequence with the seed value
        sequence = []
        Xi = seed

        # Generate the sequence for the given count
        for _ in range(count):
            Xi = (a * Xi + c) % m  # LCG formula
            sequence.append(Xi)

        return sequence

    except TypeError as te:
        print(f"Type Error: {te}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    a = 2175143      # multiplier
    seed = 3553   # seed value
    c = 10653      # increment
    m = 1000000     # modulus
    count = 10  # number of values to generate

    sequence = linear_congruential_generator(a, seed, c, m, count)
    
    if sequence:
        print(f"Generated sequence: {sequence}")
