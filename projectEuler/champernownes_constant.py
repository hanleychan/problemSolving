"""
An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

if __name__ == "__main__":
    number_string = ""
    next_number = 1

    # Generate number 123456789101112 ...
    while(len(number_string) < 1000000):
        number_string = number_string + str(next_number)
        next_number += 1

    # convert number to a list of digits
    digit_list = list(map(lambda x: int(x), number_string))

    d1 = digit_list[0]
    d10 = digit_list[9]
    d100 = digit_list[99]
    d1000 = digit_list[999]
    d10000 = digit_list[9999]
    d100000 = digit_list[99999]
    d1000000 = digit_list[999999]

    print(d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000)
