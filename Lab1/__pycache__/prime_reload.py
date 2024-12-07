import math

def prime_number(limit):
    try:
        # Ensure that the limit is a positive integer
        if not isinstance(limit, int):
            raise TypeError("Limit must be an integer.")
        if limit <= 1:
            raise ValueError("Limit must be greater than 1.")
        
        # Start with known primes 2 and 3
        primes = []
        if limit >= 2:
            primes.append(2)
        if limit >= 3:
            primes.append(3)
        
        # Use 6k ± 1 rule for numbers > 3
        for n in range(1, (limit // 6) + 1):
            # 6k - 1
            val1 = 6 * n - 1
            if val1 < limit and is_prime(val1):
                primes.append(val1)
            
            # 6k + 1
            val2 = 6 * n + 1
            if val2 < limit and is_prime(val2):
                primes.append(val2)
        
        primes = sorted(set(primes))  # Sort and remove duplicates
        return primes
    
    except TypeError as te:
        print(f"Type Error: {te}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def is_prime(n):
    """ Helper function to check if a number is prime """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisibility from 5 to sqrt(n) skipping multiples of 2 and 3
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

# Test cases: Calculate primes up to 1000
limit = 1000
prime_list = prime_number(limit)

if prime_list:
    print(f"Prime numbers up to {limit}:")
    print(prime_list)
else:
    print(f"No primes found up to {limit}.")
