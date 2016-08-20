"""
Find the sum of all the primes below 2,000,000
"""

import math

def is_prime(n):
    """ Returns whether n is a prime number """
    
    for i in range(2, int(math.sqrt(n)) + 1): # every non-prime # is divisible by a prime <= sqrt(#)
        if n % i == 0:
            return False
    else:
        if n <= 1:
            return False
        else:
            return True

number = 2000000
total = 0

for i in range(2, number + 1):
    if is_prime(i):
        total += i 
print(total)
