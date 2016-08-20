"""
Find the largest palindrome made from the product of two 3-digit numbers
"""

def is_palindrome_number(n):
    """ Returns whether a number is a palindrome """ 
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

def can_be_made_by_multiplying_3_digit_numbers(n):
    """ Returns whether a number can be made by multiplying 2 3 digit numbers """
    for i in range(100,1000):
        if n % i == 0:
            if n / i >= 100 and n / i <= 999:
                return True
    else:
        return False


for i in range((100*100), (999*999)+1)[::-1]:
    if is_palindrome_number(i):
        if can_be_made_by_multiplying_3_digit_numbers(i):
            print(i)
            break

