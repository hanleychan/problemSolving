"""
The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

from math import sqrt

def is_prime(n):
    """ Returns whether n is a prime number """
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        if n <= 1:
            return False
        else:
            return True

def get_prime_factors(n):
    """ Returns a list of the prime factors of n """
    if n <= 1:
        return []

    result = []

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                result.append(i)
            if i * i != n and is_prime(int(n/i)):
                result.append(int(n/i))

    return result

if __name__ == "__main__":
    results = []
    number = 1
    while True:
        if len(get_prime_factors(number)) == 4:
            results.append(number)
        else:
            results = []

        if len(results) == 4:
            break

        number += 1

    print(results)
