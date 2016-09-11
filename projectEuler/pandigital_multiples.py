"""
Find the largest 1 to 9 pandigital 9 digit number that can be formed as the concatenated
product of an integer with (1,2,...,n) where n > 1
"""

from math import sqrt

def is_pandigital(n):
    """ Returns whether a number is 1 through 9 pandigital """
    number_string = str(n)
    number_list = [int(x) for x in number_string]


    if len(number_string) != 9:
        return False

    for i in range(1, 10):
        if i not in number_list:
            return False

    return True

def concat_numbers(num_1, num_2):
    """ Concatenates two numbers """
    number_string_1 = str(num_1)
    number_string_2 = str(num_2)

    return int(number_string_1 + number_string_2)


if __name__ == "__main__":
    pandigital_numbers = []
    upper_bound = 9999 # if n > 4 digits, concatenating (n * 1 + n * 2) > 9 digits

    for i in range (1, upper_bound):
        number = i
        multiplier = 2
        while (len(str(number)) < 9):
            number = concat_numbers(number, i  * multiplier)
            multiplier += 1

        if is_pandigital(number):
            pandigital_numbers.append(number)

    print(max(pandigital_numbers))
