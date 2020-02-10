#Author: Anthony Ferrari
#Description: Sudoku solver with print function



grid = [[0 for x in range(9)]for y in range(9)]

def print_grid(arr):
    total_rows = len(arr)
    first_row = len(arr[0])
    for row in range(total_rows):
        #every third row we will print the horizontal divider
        if row % 3 == 0 and row in range(1,10):
            print("- - - - - - - - - - - - - - - - -")
        #for every third column we will print a vertical divider
        for col in range(first_row):
            if col % 3 == 0 and col in range(1,10):
                print(" | ", end=" ")
            if col == 8:
                print(arr[row][col])
            else:
                print(str(arr[row][col]) + " ", end=" ")

def empty_spot(arr):
    # first_row = len(arr[0])
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                return row, col
    return False
def valid_position(arr, num, pos):
    first_row = len(arr[0])
    #check col
    for col in range(first_row):
        if arr[pos[0]][col] == num and pos[1] != col:
            return False

    #check row
    total_rows = len(arr)
    for row in range(total_rows):
        if arr[row][pos[1]] == num and pos[0] != row:
            return False

    #check box
    #check to see if this can be simplified
    beginning_row = pos[0] - pos[0]%3
    beginning_column = pos[1] - pos[1]%3

    for row in range(3):
        for col in range(3):
            if arr[row+beginning_row][col+beginning_column] == num and (row, col) != pos:
                return False
    return True


def solve_algo(arr):
    #uses all definitions except print_grid

    #looks for empty spots
    finder = empty_spot(arr)
    if finder:
        row, col = finder
    else:
        return True
    for i in range(1, 10):
        if valid_position(arr, i, (row, col)):
            arr[row][col] = i

            if solve_algo(arr):
                return True
            arr[row][col] = 0

    return False


print_grid(grid)
solve_algo(grid)
print("_________________________________")
print_grid(grid)