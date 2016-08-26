"""
Find the sum of the digits in the number 100!
"""

def factorial(n):
    """ Returns the result n! """
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n-1)



if __name__ == "__main__":
    # find 100!
    number = factorial(100)

    
    total = 0

    # add the value of each digit to total
    for digit in str(number):
        total += int(digit)

    print(total)

