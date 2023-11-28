"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be a positive integer")

    prime_list = []
    num = 2  # Start with the first prime number

    while len(prime_list) < number_of_primes:
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
        num += 1

    return prime_list
