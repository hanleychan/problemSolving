"""
Find the sum of all the amicable numbers under 10000
"""

from math import sqrt

def get_sum_proper_divisors(n):
    """ Returns the sum of the proper divisors of n """
    result = 0

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result += i

            if int(n/i) != i and i != 1:
                result += int(n/i)
    return result

def get_amicable_pair(n):
    """ Returns n's amicable pair n is an amicable number """
    sum_proper_divisors = get_sum_proper_divisors(n)
    if get_sum_proper_divisors(sum_proper_divisors) == n and sum_proper_divisors != n:
		
        return sum_proper_divisors
    else:
        return False

if __name__ == "__main__":
    amicable_numbers = []
    for i in range(10001):
        if i in amicable_numbers:
            continue

        amicable_pair = get_amicable_pair(i)
        if amicable_pair:
            amicable_numbers.extend((i, amicable_pair))

    total = 0
    for i in amicable_numbers:
        total += i
    print(total)
