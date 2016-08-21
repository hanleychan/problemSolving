"""
Find the sum of the even valued terms in the Fibonacci sequence that are under four million 

First 10 terms: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

"""

def is_even(n):
    """ Returns whether n is an even number """
    return n % 2 == 0

def fibonacci(n):
    """ Find the fibonacci value at position n """
    if n == 1 or n == 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    result = 0
    index = 1

    while fibonacci(index) < 4000000:
        if is_even(fibonacci(index)):
            result += fibonacci(index)

        index += 1

    print(result)
