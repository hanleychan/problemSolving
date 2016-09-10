"""
Find the sum of all numbers which are equal to the sum of the factorial of their digits
"""

def factorial(n):
    """ Returns the value of n! """
    if n == 0:
        return 1

    result = 1
    for i in range(2, n+1):
        result *= i

    return result


if __name__ == "__main__":
    upper_bound = factorial(9) * 7 # 2540160, 10^(d-1) <= n <= 9!d, 7 is the largest value that satisfies d

    results = []

    for number in range(3, upper_bound):
        sum_factorials = 0
        for digit in str(number):
            sum_factorials += factorial(int(digit))

        if sum_factorials == number:
            results.append(number)

    print(sum(results))
