"""
Using names.txt, sort the names into alphabetical order. Then work out the alphabetical
value for each name.  Multiply this value by its alphabetical position in the list to obtain
a name score.

Find the total of all the name scores in the file
"""
import re
import string

def get_alphabetic_value(name, position):
    """ Returns the alphabetic value of a name """
    alphabet = string.ascii_uppercase # ABC..XYZ
    letter_scores = {}

    for index, letter in enumerate(alphabet):
        letter_scores[letter] = index + 1

    total_score = 0
    for letter in name.upper():
        total_score += letter_scores[letter]

    return total_score * position

if __name__ == "__main__":
    # open and read the names file
    with open("names.txt", "r") as my_file:
        names = my_file.read()

    # remove double quote marks from names
    names = names[1:len(names)-1]
    names = re.sub(r'","', ",", names) 

    # sort names into a list
    names_list = sorted(names.split(","))

    total_score = 0
    for index, name in enumerate(names_list):
        total_score += get_alphabetic_value(name, index + 1)

    print(total_score)
        

