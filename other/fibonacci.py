"""
Write a function to find n value in the sequence:  1, 2, 3, 5, 8, 13, 21, ..., n
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
