"""
Starting in the top left corner and only being able to move right and down, find the number of routes
through a 20x20 grid.
"""

if __name__ == "__main__":
    num_rows = 20 
    num_cols = 20 

    num_paths_to_points = {}

    # 1 way to get to each of the top-most and left-most points
    for x in range(num_rows + 1):
        num_paths_to_points[(x, 0)] = 1 
    for y in range(num_cols + 1):
        num_paths_to_points[(0,y)] = 1

    # # of ways to get to each point = sum(ways to get to points above and to the left of the point)
    for x in range(1, num_rows + 1):
        for y in range(1, num_cols + 1):
           num_paths_to_points[(x, y)] = num_paths_to_points[x-1, y] + num_paths_to_points[x, y-1]

    print(num_paths_to_points[num_rows, num_cols])

