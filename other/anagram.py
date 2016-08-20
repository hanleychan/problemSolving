"""
Write a function that determines if two words are anagrams
"""

def anagram(word1, word2):
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    if sorted_word1 == sorted_word2:
        return True
    else:
        return False
