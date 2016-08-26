"""
By starting at the top of the triangle and moving to adjacent numbers on the row
below, find the maximum total from top to bottom of the triangle below:

                 75
                95 64
               17 47 82
              18 35 87 10
             20 04 82 47 65
            19 01 23 75 03 34
           88 02 77 73 07 63 67
          99 65 04 28 06 16 70 92
         41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
       53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
     91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
   04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def get_path_sum(path, number_triangle):
    """ Returns the sum of a path """
    path_sum = 0
    for node in path:
        path_sum += number_triangle[node[0]][node[1]]
    return path_sum


def find_sum(number_triangle):
    """ Returns the sum of the largest path in the triangle """
    curr_row = 0
    curr_col = 0
    num_rows = len(number_triangle)
    num_cols = len(number_triangle[num_rows-1])
    curr_path = [[0,0]] # start at the top node
    visited_paths_going_right = [] # keep track of paths after moving right
    path_max = 0

    while not (curr_row == num_rows - 1 and curr_col == (num_cols -1)):
        # go left it not on bottom row
        if curr_row + 1 < num_rows:
            # go down to the left until reach bottom node
            while curr_row < num_rows - 1:
                curr_row += 1
                curr_path.append([curr_row, curr_col])

            # reached buttom, update maximum sum if > than current maximum
            path_sum = get_path_sum(curr_path, number_triangle)
            path_max = max(path_max, path_sum)

            # backtrack one node up and update current node location
            curr_path.pop()
            curr_row, curr_col = tuple(curr_path[-1])


        # backtrack up until can move down to the right to a valid path that hasn't already been visited
        while curr_path + [[curr_row+1, curr_col+1]] in visited_paths_going_right or curr_row + 1 == num_rows:
            curr_path.pop()
            curr_row, curr_col = tuple(curr_path[-1])
        

        # go right once
        if curr_row + 1 < num_rows and curr_col + 1 < num_cols:
            curr_row += 1
            curr_col += 1
            visited_paths_going_right.append(curr_path + [[curr_row, curr_col]])
            curr_path.append([curr_row, curr_col])

            # reached bottom row, update maximum sum if > than current maximum
            path_sum = get_path_sum(curr_path, number_triangle)
            path_max = max(path_max, path_sum)
                
    return path_max

if __name__ == "__main__":
    number_triangle = [
                [75],
                [95,64],
                [17,47,82],
                [18, 35, 87, 10],
                [20, 4, 82, 47, 65],
                [19, 1, 23, 75, 3, 34],
                [88, 2, 77, 73, 7, 63, 67],
                [99, 65, 4, 28, 6, 16, 70, 92],
                [41, 41, 26, 56, 83, 40, 80, 70, 33],
                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
            ]


    result = find_sum(number_triangle)
    print(result)
