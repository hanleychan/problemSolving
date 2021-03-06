"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal 
numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, 
is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are 
pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
"""
from math import sqrt 

def generate_pentagon_numbers(start_index = 1, n = 10):
    """ Generates n pentagon number starting from start_index """
    pentagon_numbers = []
    if n <= 0 or start_index < 1:
        return []

    for i in range(start_index, start_index + n):
        next_number = int((i * (3 * i - 1)) / 2)
        pentagon_numbers.append(next_number)

    return pentagon_numbers

def is_pentagon_number(n):
    """ Returns whether n is a pentagon number """
    k = (sqrt(24 * n + 1) + 1) / 6 # pentagon number if k is an integer

    # check if k is an integer
    if k == int(k):
        return True
    else:
        return False

if __name__ == "__main__":
    # Start with  first 2 pentagon numbers
    pentagon_numbers = generate_pentagon_numbers(1, 2)
    
    result_found = False
    index = 1
    while True:
        for pentagon_number in pentagon_numbers[:len(pentagon_numbers) - 1]:
            if (is_pentagon_number(pentagon_number + pentagon_numbers[index]) and 
                is_pentagon_number(pentagon_numbers[index] - pentagon_number)):
                    result = abs(pentagon_numbers[index] - pentagon_number)
                    result_found = True
                   
        if result_found:
            break
        else:
            # get next pentagon number and update index position
            pentagon_numbers.extend(generate_pentagon_numbers(len(pentagon_numbers) + 1, 1))
            index += 1

    print(result)
