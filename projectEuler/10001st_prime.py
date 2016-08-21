"""
Find the 10,001st prime number
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

if __name__ == '__main__':
    prime_counter = 0
    number = 2
    while prime_counter < 10001:
        if is_prime(number):
            prime_counter += 1

            if prime_counter == 10001:
                break

        number += 1

    print(number)
