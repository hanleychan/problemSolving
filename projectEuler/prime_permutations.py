"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 
3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each 
of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from math import sqrt

def is_prime(n):
    """ Returns whether n is a prime number """
    if n <= 1:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def same_digits(num1, num2):
    """ Returns whether num1 and num2 are made with the same digits """
    if len(str(num1)) != len(str(num2)):
        return False

    num1_list = []
    num2_list = []

    for digit in str(num1):
        num1_list.append(int(digit))

    for digit in str(num2):
        num2_list.append(int(digit))

    for digit in num2_list:
        if digit not in num1_list:
            return False

    return True

if __name__ == "__main__":
    first_num = 1000

    while True:
        # keep incrementing first_num until it is a prime number
        while not is_prime(first_num):
            first_num += 1

        if first_num == 1487:
            first_num += 1

        second_num = first_num + 3330

        # second number doesn't satisfy condition.  
        if not is_prime(second_num) or not same_digits(first_num, second_num):
            first_num += 1
            continue

        third_num = second_num + 3330

        # third number satisfies condition
        if is_prime(third_num) and same_digits(first_num, third_num):
            break

        first_num += 1

    result = int(str(first_num) + str(second_num) + str(third_num))
    print(result)
