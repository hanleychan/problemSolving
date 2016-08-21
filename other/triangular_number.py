"""
Write a function that returns the nth triangular number
"""

def triangular_number(n):
    result = sum(list(range(1,n+1)))
    return result

