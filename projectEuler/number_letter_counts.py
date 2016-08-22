"""
Find the number of letters used if all the numbers from 1 to 1000 inclusive were written out in words
"""

import re

def number_to_words():
    """ Returns a dictionary of numbers mapped to it's word equivalent form from 1 - 1000 """

    number_words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                    11: "eleven", 12: "twelve", 13: "thirteen", 15: "fifteen", 18: "eighteen",
                    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 80: "eighty",
                    1000: "one thousand"}
   

    # set number_words for numbers 14-19 that are not set
    for i in range(14, 20):
        ones_digit = int(str(i)[-1])

        # skip special cases that are already set: 15 & 18 
        if ones_digit in [5,8]:
            continue
        number_words[i] = number_words[ones_digit] + "teen"
    
    # set number_words for numbers 60-90 that are not set
    for i in range(60, 91, 10):
        tens_digit = int(str(i)[-2])

        # skip special cases that are already set: 80
        if tens_digit in [8]:
            continue
        number_words[i] = number_words[tens_digit] + "ty"

    for i in range(1, 1000):
        if i in number_words:
            continue
        str_num = str(i)

        if len(str_num) == 2: # Set 21 - 99
            number_words[i] = number_words[int(str_num[-2] + "0")]
            if str_num[-1] != "0":
                number_words[i] = number_words[i] + "-" + number_words[int(str_num[-1])]
        elif len(str_num) == 3: # Set 100 - 999
            number_words[i] = number_words[int(str_num[-3])] + " hundred"
            if str_num[1:] != "00":
                number_words[i] = number_words[i] + " and " + number_words[int(str_num[1:])]

    return number_words

def strip_spaces_dashes(word):
    """ Strips all the spaces and dashes from a string """
    return re.sub(r'[-\s]', '', word)


if __name__ == "__main__":
    number_words = number_to_words()

    total = 0
    for word in number_words:
        total += len(strip_spaces_dashes(number_words[word]))

    print(total)
