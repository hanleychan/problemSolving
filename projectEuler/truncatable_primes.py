"""
Find the sum of the only eleven primes that are both truncatable from left to right and right to left
"""

from math import sqrt, floor

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

def truncate_left(n):
    """ truncates the left digit of a number """
    number_string = str(n)
    
    if len(number_string) == 1:
        return 0
    else:
        return int(number_string[1:])

def truncate_right(n):
    """ truncates the right digit of a number """
    return floor(n * 0.1)

def truncatable_prime(n):
    """ returns whether n is a truncatable prime """
    if n < 10 or not is_prime(n): # 2,3,5,7 are not truncatable primes
        return False

    truncate_left_number = n
    while(len(str(truncate_left_number)) != 1):
        truncate_left_number = truncate_left(truncate_left_number)
        if not is_prime(truncate_left_number):
            return False

    truncate_right_number = n
    while(len(str(truncate_right_number)) != 1):
        truncate_right_number = truncate_right(truncate_right_number)
        if not is_prime(truncate_right_number):
            return False

    return True

if __name__ == '__main__':
    truncatable_primes = []
    
    number = 10
    while(len(truncatable_primes) != 11):
        if truncatable_prime(number):
            truncatable_primes.append(number)
        number += 1

    print(sum(truncatable_primes))
