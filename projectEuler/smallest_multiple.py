"""
Find the smallest positive number that is evenly divisible by all the numbers from 1 to 20
"""

number = 20

while True:
    for i in range(2, 21):
        if number % i != 0:
            break
    else:
        break
    number += 20

print(number)
