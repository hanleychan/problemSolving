"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

def get_num_solutions(perimeter):
    """ Returns the number of solution combinations given a perimiter of a right triangle """
    a, b, c = 1, 1, 1
    solutions = []

    while a <= perimeter: # Loop through all possible values of a
        old_b = b

        while b <= perimeter - a: # Loop through all possible values of b
            c = perimeter - b - a
            
            if a*a + b*b == c*c and (b,a,c) not in solutions:
                solutions.append((a,b,c))
            
            if b + 1 <= perimeter - a:
                b += 1     
            else:
                break

        a += 1
        b = old_b 
        c = 1

    return len(solutions)

if __name__ == "__main__":
    max_solutions_perimeter = 0
    max_solutions = 0

    for p in range(1001):
        num_solutions = get_num_solutions(p)
        if num_solutions > max_solutions:
            max_solutions_perimeter = p
            max_solutions = num_solutions

    print(max_solutions_perimeter)
