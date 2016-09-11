"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""

def find_abc_pythagorean(perimeter):
    """ Returns the first values of a,b and c such that a**2 + b**2 = c**2 
    given the perimeter value """
    a, b, c = 1, 1, 1

    while a <= perimeter: # Loop through all possible values of a
        old_b = b

        while b <= perimeter - a: # Loop through all possible values of b
            c = perimeter - b - a
            
            if a*a + b*b == c*c:
                return a,b,c 

            if b + 1 <= perimeter - a:
                b += 1     
            else:
                break

        a += 1
        b = old_b 
        c = 1
    else: # No value found
        return False

if __name__ == "__main__":
    result = find_abc_pythagorean(1000)

    if result:
        print(result[0] * result[1] * result[2])
