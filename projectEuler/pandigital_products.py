"""
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 
1 through 9 pandigital
"""

from math import sqrt

def get_multiplicand_and_multiplier(number):
    """ Returns a list of multiplicand and multiplier values that equal to the number """
    result = []

    for i in range(1, int(sqrt(number))+1):
        if number % i == 0:
            result.append((i, int(number/i)))

    return result

def one_through_nine_pandigital(number):
    """ Returns whether the combination of multiplicand, multiplier and product is pandigital """
    numbers_list = []
    numbers = get_multiplicand_and_multiplier(number)

    for digit in str(number):
        if int(digit) in numbers_list or int(digit) == 0:
            return False
        else:
            numbers_list.append(int(digit))

    for num_1, num_2 in numbers:
        temp_numbers_list = numbers_list[:]
        
        restart = False
        for digit in str(num_1):
            if int(digit) in temp_numbers_list or int(digit) == 0:
                restart = True
                break
            else:
                temp_numbers_list.append(int(digit))

        if restart:
            continue

        for digit in str(num_2):
            if int(digit) in temp_numbers_list or int(digit) == 0:
                restart = True
                break
            else:
                temp_numbers_list.append(int(digit))

        if restart:
            continue

        if len(temp_numbers_list) == 9:
            return True
    else:
        return False


if __name__ == "__main__":
    results = []

    upper_bound = 98765
    for number in range(1, upper_bound):
        if one_through_nine_pandigital(number):
            results.append(number)

    print(sum(results))
