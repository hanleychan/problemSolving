"""
Find the 10,001st prime number
"""
def is_prime(n):
    """ Returns whether n is a prime number """
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        if n <= 1:
            return False
        else:
            return True

prime_counter = 0
number = 2
while prime_counter < 10001:
    if is_prime(number):
        prime_counter += 1

        if prime_counter == 10001:
            break

    number += 1

print(number)
