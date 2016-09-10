"""
Find the number of circular primes below one million
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

def rotate_digits(n, num_digits):
    """ Moves the digit at the start to the end of the number """

    number_list = list(str(n))

    # Check if 0 was rotated out previously
    if len(number_list) < num_digits:
        number_list.append("0")
    else:
        first_digit = number_list.pop(0)
        number_list.append(first_digit)
    
    result = int("".join(number_list))
    return result

def is_circular_prime(n):
    """ Returns whether a n is a circular prime """
    if not is_prime(n):
        return False
    else:
        number_string = str(n)
        
        num_digits = len(str(n))
        times_to_rotate = num_digits - 1

        for i in range(times_to_rotate):
            n = rotate_digits(n, num_digits)
            if not is_prime(n):
                return False

    return True

if __name__ == "__main__":
    circular_primes = []
    for number in range(1,1000000):
        if is_circular_prime(number):
            circular_primes.append(number)

    print(len(circular_primes))
