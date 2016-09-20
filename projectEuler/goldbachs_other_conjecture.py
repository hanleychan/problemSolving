"""
Find the smallest odd composite that cannot be written as the sum of a prime and
twice a square
"""

from math import sqrt

def is_prime(n):
    """ Returns whether n is a prime number """
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        if n <= 1:
            return False
        else:
            return True

if __name__ == "__main__":
    number = 9 # first possible odd composite number
    twice_square_numbers = [2]

    while True:
        # update twice_square_numbers until > number
        while twice_square_numbers[-1] < number:
            twice_square_numbers.append(2 * ((len(twice_square_numbers) + 1) ** 2))

        goldbachs_other_conjecture = True 

        for twice_square_number in twice_square_numbers[:len(twice_square_numbers) - 1]:
            temp = number - twice_square_number 

            if is_prime(temp):
                # goldbachs other conjecture holds.  
                break
        else:
            # Loop completed without finding a condition where goldbachs other conjecture holds
            goldbachs_other_conjecture = False

        if goldbachs_other_conjecture == False:
            break

        # get next odd composite number
        number += 2
        if is_prime(number):
            number += 2

    print(number)
