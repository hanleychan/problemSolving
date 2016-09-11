"""
Find the largest n-digit pandigital prime that exists
"""

from math import sqrt

def is_pandigital(n):
    """ Returns whether a number is pandigital """
    number_string = str(n)
    number_list = [int(x) for x in number_string]

    if len(number_string) > 9:
        return False

    for i in range(1, len(number_string) + 1):
        if i not in number_list:
            return False

    return True

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

def is_pandigital_prime(n):
    """ Returns whether n is a pandigital prime """
    return is_pandigital(n) and is_prime(n)

if __name__ == "__main__":
    # integers divisible by 3 has it's sum of digits divisible by 3 => prime# must be 4 or 7 digits
    lower_bound = 1234567 # smallest 7 digit pandigital #
    upper_bound = 7654321 # largest 7 digit pandigital #

    for i in range(lower_bound, upper_bound + 1)[::-1]:
        if is_pandigital_prime(i):
            largest = i
            break
    else:
        # if no 7 digital pandigital prime found, try 4 digits
        lower_bound = 1234
        upper_bound = 4321

        for i in range(lower_bound, upper_bound + 1)[::-1]:
            if is_pandigital_prime(i):
                largest = i
                break

    print(largest)
