"""
Find the largest prime factor of the number 600851475143
"""
number = 600851475143

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

def is_factor_of_number(n):
    """ Returns whether n is a factor of number """
    if number % n == 0:
        return True
    else:
        return False

largest_prime_factor = 0;
for i in range(2,int((number/2))):
    if is_factor_of_number(i):
        if is_prime(int(number/i)):
            largest_prime_factor = int(number/i)
            break
        else:
            if is_prime(i):
                largest_prime_factor = i

print(largest_prime_factor)
