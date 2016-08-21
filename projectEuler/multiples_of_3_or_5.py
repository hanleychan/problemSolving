"""
Finds the sum of all the multiples of 3 or 5 below 1000
"""

def multiple_of_3_or_5(n):
    """ Returns whether n is a multiple of 3 or 5 """
    if n % 3 == 0 or n % 5 == 0:
        return True
    return False

if __name__ == "__main__":
    result = 0
    for i in range(1, 1000):
        if multiple_of_3_or_5(i):
            result += i

    print(result)

