"""
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits
"""

def sum_of_fifth_powers(n):
    """ Returns whether n can be written as the sum of the fifth powers of its digits """

    if n <= 1:
        return False

    result = 0

    for digit in str(n):
        result += int(digit) ** 5

    if result == n:
        return True
    else:
        return False



if __name__ == "__main__":
    upper_bound = 9**5 * 6
    results = []
    
    for n in range(2, upper_bound):
        if sum_of_fifth_powers(n):
            results.append(n)

    print(sum(results))
