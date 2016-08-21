"""
Find the sum of the digits of the number 2**1000
"""

if __name__ == "__main__":
    number = 2 ** 1000
    total = 0

    for digit in str(number):
        total += int(digit)

    print(total)
