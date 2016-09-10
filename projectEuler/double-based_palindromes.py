"""
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
"""

def is_palindrome(number):
    """ Returns whether a number is palindromic in both base 10 and 2 """
    number_string = str(number)
    if not number_string == number_string[::-1]:
        return False

    binary_string = bin(number)[2:]
    if not binary_string == binary_string[::-1]:
        return False

    return True

if __name__ == "__main__":
    palindromic_numbers = []
    for number in range(1, 1000000):
        if is_palindrome(number):
            palindromic_numbers.append(number)

    print(sum(palindromic_numbers))
