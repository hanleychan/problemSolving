"""
Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum
"""

sum_of_squares = 0
square_of_the_sum = 0

for i in range(1,101):
    sum_of_squares += i ** 2
    square_of_the_sum += i

square_of_the_sum = square_of_the_sum ** 2

result = square_of_the_sum - sum_of_squares

print(result)

