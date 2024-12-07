import sys

def sieve_for_primes_to(n):
    """ Return all primes up to n using the Sieve of Eratosthenes """
    try:
        # Validate the input is an integer greater than 1
        if not isinstance(n, int):
            raise TypeError("Input must be an integer.")
        if n < 2:
            raise ValueError("Input must be greater than or equal to 2.")
        
        size = n // 2  # We'll only handle odd numbers > 2
        sieve = [1] * size  # Sieve initialization for odd numbers

        limit = int(n**0.5)  # The limit to check for factors
        for i in range(1, (limit // 2) + 1):
            if sieve[i]:
                val = 2 * i + 1
                tmp = ((size - 1) - i) // val
                sieve[i + val::val] = [0] * tmp

        # Return list of primes, starting with 2, then the odd primes
        return [2] + [2 * i + 1 for i, v in enumerate(sieve) if v and i > 0]

    except TypeError as te:
        print(f"Type Error: {te}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution with command-line argument handling
if __name__ == "__main__":
    try:
        # Set default test value or take input from command-line
        test = 1000
        if len(sys.argv) > 1:
            test = int(sys.argv[1])
        
        primes = sieve_for_primes_to(test)
        
        if primes:
            print(f"Primes up to {test}:")
            print(primes)
        else:
            print(f"No primes found up to {test}.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
