import math

def is_prime(num):
    """
    Checks if a number is prime
    """
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

def generate_primes(n):
    """
    Generates a list of prime numbers up to n
    """
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

def generate_twin_primes(primes):
    """
    Generates a list of twin prime pairs
    """
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i + 1]))
    return twin_primes

def find_largest_prime_gap(twin_primes):
    """
    Finds the largest gap between twin prime pairs
    """
    largest_gap = 0
    for i in range(len(twin_primes) - 1):
        gap = twin_primes[i + 1][0] - twin_primes[i][1]
        if gap > largest_gap:
            largest_gap = gap
    return largest_gap

if __name__ == "__main__":
    primes = generate_primes(1000000000000000)
    twin_primes = generate_twin_primes(primes)
    largest_gap = find_largest_prime_gap(twin_primes)
    print(largest_gap)
