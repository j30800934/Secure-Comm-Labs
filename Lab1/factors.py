def prime_factors(n):
    factors = []
    
    # Divide n by 2 until it's odd
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Now check for odd factors from 3 upwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
     # Join the factors with '×' instead of commas
    return ' × '.join(map(str, factors))

# Example usage
number = 68367362
prime_factors_of_number = prime_factors(number)
print(f"Prime factors of {number}: {prime_factors_of_number}")

