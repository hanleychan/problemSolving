"""
Find the millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,7,8,9
"""

if __name__ == "__main__":
    number = [0,1,2,3,4,5,6,7,8,9]

    for i in range(999999):
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

                # move the smallest digit larger the spot before the spot
                number.insert(index-1, number.pop(smallest_num_position))

                # sort the digits to the right of the moved digit to form the next permutation
                number = number[:index] + sorted(number[index:])
                break

            index -= 1

    result = int("".join([str(x) for x in number]))
    print(result)
    


