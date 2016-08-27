"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
"""

from math import sqrt

def is_abundant_num(n):
    """ Returns whether n is an abundant number """
    sum_divisors = 0
    for i in range (1, int(sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i

            if i * i != n and i != 1:
                sum_divisors += int(n/i)

    if sum_divisors > n:
        return True
    else:
        return False


def get_abundant_nums(n):
    """ Returns a list of all abundant numbers up to n """
    abundant_nums = []

    for i in range(1, n):
        if is_abundant_num(i):
            abundant_nums.append(i)

    return abundant_nums

def get_abundant_sums(n):
    """ Returns the sums of all pairs of abundant numbers where the result is < n """
    abundant_nums = get_abundant_nums(n + 1)
    abundant_sums = set() 

    # find all sums of abundant numbers that are under n 
    for i in abundant_nums:
        for j in abundant_nums:
            if i + j > n:
                break
            if i + j not in abundant_sums:
                abundant_sums.add(i + j)

    return abundant_sums


if __name__ == "__main__":
    max_num = 28123

    abundant_sums = get_abundant_sums(max_num)

    total_sum = 0
    for i in range(1, max_num + 1):
        if i not in abundant_sums:
            total_sum += i

    print(total_sum)
