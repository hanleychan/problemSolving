"""
Starting with the number 1 and moving to the right in a clockwise direction, find the sum
of the numbers on the diagonals in a 1001 by 1001 spiral

5 by 5 spiral:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""

from math import sqrt

def generate_grid(size):
    """ Returns a dictionary of the grid locations and number its values """
    grid = {}
    grid_size = size * size 
    current_row =  size // 2
    current_col =  size // 2

    grid[current_row, current_col] = 1
    travel_direction = "RIGHT"
    travel_distance = 1
    next_number = 2

    while next_number <= grid_size:
        for steps in range(travel_distance):
            if travel_direction == "RIGHT":
                current_col += 1
            elif travel_direction == "LEFT":
                current_col -= 1
            elif travel_direction == "DOWN":
                current_row += 1
            elif travel_direction == "UP":
                current_row -= 1

            grid[(current_row, current_col)] = next_number
            next_number += 1

            if next_number > grid_size:
                break

        # update direction and travel distance
        if travel_direction == "RIGHT":
            travel_direction = "DOWN"
        elif travel_direction == "DOWN":
            travel_direction = "LEFT"
            travel_distance += 1
        elif travel_direction == "LEFT":
            travel_direction = "UP"
        elif travel_direction == "UP":
            travel_direction = "RIGHT"
            travel_distance += 1

    return grid

def calculate_diagonal_sum(grid):
    """ Returns the sum of the diagonals of a grid """
    size = int(sqrt(len(grid)))
    diagonals = []

    # Get numbers starting from the top left (0,0) to the bottom right (size-1, size-1)
    current_row = 0
    current_col = 0
    while current_row <= (size-1) and current_col <= (size-1):
        diagonals.append(grid[current_row, current_col])
        current_row += 1
        current_col += 1

    # Get numbers starting from the bottom left (size-1, 0) to the top right (0, size-1)
    current_row = size-1
    current_col = 0
    while current_row >= 0 and current_col <= (size-1):
        # middle grid location already added in previous loop. Skip
        if not(current_row == (size//2) and current_col == (size//2)):
            diagonals.append(grid[current_row, current_col])

        current_row -= 1
        current_col += 1

    return sum(diagonals)


if __name__ == "__main__":
    size = 1001 
    grid = generate_grid(size)
    result = calculate_diagonal_sum(grid)

    print(result)

