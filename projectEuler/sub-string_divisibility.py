"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the 
digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
"""

if __name__ == "__main__":
    number = list(range(10)) # [0,1,2,3,4,5,6,7,8,9]
    results = []

    # keep finding the next number in the permutation until the largest possible pandigital reached
    while number != list(range(10))[::-1]:
        # find the next number in the permutation
        index = len(number) - 1
        while index > 0:
            # find first spot from the right where left digit is smaller than right digit
            if int(number[index-1]) < int(number[index]):
                # find the smallest digit to the right larger than the digit at the spot found
                smallest_num = number[index]
                smallest_num_position = index
                    
                for i, digit in enumerate(number[index:]):
                    if digit < smallest_num and digit > number[index-1]:
                        smallest_num = digit
                        smallest_num_position = index + i 

                # move the smallest digit larger than the spot before the spot
                number.insert(index-1, number.pop(smallest_num_position))

                # sort the digits to the right of the moved digit to form the next permutation
                number = number[:index] + sorted(number[index:])
                break
            index -= 1

        # check divisibility conditions
        d2_d4 = number[1:4]
        if int("".join([str(x) for x in d2_d4])) % 2 != 0:
            continue

        d3_d5 = number[2:5]
        if int("".join([str(x) for x in d3_d5])) % 3 != 0:
            continue

        d4_d6 = number[3:6]
        if int("".join([str(x) for x in d4_d6])) % 5 != 0:
            continue

        d5_d7 = number[4:7]
        if int("".join([str(x) for x in d5_d7])) % 7 != 0:
            continue

        d6_d8 = number[5:8]
        if int("".join([str(x) for x in d6_d8])) % 11 != 0:
            continue

        d7_d9 = number[6:9]
        if int("".join([str(x) for x in d7_d9])) % 13 != 0:
            continue

        d8_d10 = number[7:]
        if int("".join([str(x) for x in d8_d10])) % 17 != 0:
            continue

        results.append(int("".join([str(x) for x in number])))

    print(sum(results))
