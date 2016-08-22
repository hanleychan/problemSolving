"""
Find the last ten digits of the series 1**1 + 2**2 + 3**3 + ... + 1000**1000
"""

if __name__ == "__main__":
    total = 0

    for i in range(1, 1001):
        total += i ** i

    last_10_digits = str(total)[len(str(total)) - 10:]
    print(last_10_digits)
