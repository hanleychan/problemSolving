"""
Using words.txt containing nearly two-thousand common English words, how many are
triangle words
"""

import string

global triangle_numbers

def is_triangle_word(word):
    """ Returns whether n is a triangle word """
    word_value = get_alphabetic_value(word.upper())
    if is_triangle_number(word_value):
        return True
    else:
        return False

def is_triangle_number(n):
    """ Returns whether n is a triangle number """
    while n > triangle_numbers[-1]:
        triangle_numbers.extend(generate_triangle_numbers(len(triangle_numbers) + 1, 1))

    if n in triangle_numbers:
        return True
    else:
        return False

def generate_triangle_numbers(start = 1, n = 10):
    """ Returns a list of n triangle numbers from index start """
    triangle_numbers = []

    if n <= 0 or start < 1:
        return []

    for i in range(start, start + n):
        next_number = int((1/2) * i * (i + 1))
        triangle_numbers.append(next_number)

    return triangle_numbers

def get_alphabetic_value(word):
    """ Returns the alphabetic value of a word"""
    alphabet = string.ascii_uppercase # ABC..XYZ
    letter_values = {}

    for index, letter in enumerate(alphabet):
        letter_values[letter] = index + 1

    total_value = 0
    for letter in word.upper():
        total_value += letter_values[letter]

    return total_value 

def something(test):
    test.append("COOL")

if __name__ == "__main__":
    num_triangle_words = 0
    triangle_numbers = generate_triangle_numbers()

    # open file for reading
    with open("words.txt", "r") as my_file:
        words = my_file.read()
    
    # split words into list and remove double quotes from each word
    words_list = words.split(",")
    words_list = list(map(lambda x: x[1:len(x)-1], words_list))

    for word in words_list:
        if is_triangle_word(word):
            num_triangle_words += 1

    print(num_triangle_words)
