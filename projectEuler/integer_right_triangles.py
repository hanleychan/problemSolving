"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from math import sqrt

def get_num_solutions(perimeter):
    """ Returns the number of solution combinations given a perimiter of a right triangle """
    solutions = []
    for a in range(1, perimeter):
        # from a^2+b^2=c^2 and p=a+b+c, b = (perimeter(perimeter - 2a)) / (2(perimeter - a))
        b = (perimeter * (perimeter - (2 * a))) / (2 * (perimeter - a))
        if b == int(b) and b > 0:
            c = sqrt(a**2 + b**2)

            if (int(b), a, int(c)) not in solutions:
                solutions.append((a,int(b),int(c)))

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
