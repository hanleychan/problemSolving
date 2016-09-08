"""
Find the product of the coefficients a and b for the quadratic expression that produces the maximum number
of primes for consecutive values of n starting with n = 0

    n^2 + an + b, where |a| < 1000 and |b| <= 1000
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

if __name__ == "__main__":
    max_primes = 0
    result_a = 0
    result_b = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            prime_counter = 0
            while True:
                result = n**2 + (a*n) + b
                if is_prime(abs(result)):
                    prime_counter += 1
                    n += 1
                else:
                    break

            if prime_counter > max_primes:
                result_a = a
                result_b = b
                max_primes = prime_counter

    result = result_a * result_b
    print(result)
