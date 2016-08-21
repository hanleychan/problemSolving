"""
Find the first triangle number to have over five hundred divisors
"""

from math import sqrt

def get_num_factors(n):
    """ Returns the number of factors of n """
    result = 1
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            if i * i == n:
                result += 1
            else:
                result += 2
    else:
        if n == 1:
            return 1
        else:
            result += 1
            

    return result

if __name__ == '__main__':
    index = 1
    prevNumber = 0
    number = 1

    while True:
        number = prevNumber + index
        num_factors = get_num_factors(number)

        if num_factors > 500:
            print(number)
            break

        prevNumber = number
        index += 1
