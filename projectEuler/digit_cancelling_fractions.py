"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may 
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing 
two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from math import sqrt

def get_factors(number):
    """ Returns a list of the factors of the given number """
    factors = []

    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if i * i != number:
                factors.append(int(number/i))

    factors.sort()

    return factors

def get_gcf(num_1, num_2):
    """ Returns the greatest common factor for two given numbers """
    num_1_factors = get_factors(num_1)
    num_2_factors = get_factors(num_2)

    gcf = 1

    for num_1_factor in num_1_factors[::-1]:
        if num_1_factor in num_2_factors:
            gcf = num_1_factor
            break

    return gcf

def simplify_fraction(numerator, denominator):
    """ Returns a tuple containing the simplified form of a fraction """
    gcf = get_gcf(numerator, denominator)
    simplified_numerator = int(numerator / gcf)
    simplified_denominator = int(denominator / gcf)

    return simplified_numerator, simplified_denominator

if __name__ == "__main__":
    fractions = [] # list of (numerator, denominator) tuples

    for numerator in range(10,100):
        for denominator in range(10, 100):
            if numerator >= denominator:
                continue

            numerator_tens = numerator // 10
            numerator_ones = numerator - (numerator_tens * 10)
            denominator_tens = denominator // 10
            denominator_ones = denominator - (denominator_tens * 10)

            if numerator_ones == denominator_tens:
                if denominator_ones != 0:
                    if (numerator_tens / denominator_ones) == (numerator / denominator):
                        fractions.append((numerator, denominator))

    if len(fractions) != 0:
        for index, fraction in enumerate(fractions):
            if index == 0:
                product_numerators = fraction[0]
                product_denominators = fraction[1]
            else:
                product_numerators *= fraction[0]
                product_denominators *= fraction[1]

        simplified_fraction = simplify_fraction(product_numerators, product_denominators)
        print(simplified_fraction[1])
