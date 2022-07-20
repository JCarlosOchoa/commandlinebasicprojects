def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indicies
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None # if no spaces are empty

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess aat the row/col of the puzzle is a vliad guess
    # returns True if is valid, False otherwise

    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # now the columns
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # now the square
    # trickier, but we want to get the "start" of the square
    # and iterate over the three rows / cols
    row_start = (row // 3) * 3  # finds out which "block", then multiply by 3 to get the index of the start of the block
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    # if we get here, then it is a valid guess
    return True

def solve_sudoku(puzzle):
    # solve sudoku puzzle using backtracking algorithm
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the oslution if it exists
    
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done bc no more valid inputs
    if row is None:
        return True
    
    # step 2: if there is a place to put a number, then make a guess b/w 1-9
    for guess in range(1,10):
        #step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, place the guess on the puzzle
            puzzle[row][col] = guess

            # recurse using this mutated puzzle
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        
        # step 5: if not valid OR if our guess does not solve the puzzle, then we need to 
        # backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess

    # step 6: if none of the numbers that we try work, then there is no solution to the puzzle
    return False

# let's test our implementation
if __name__ == "__main__":
    example_board = [
        [3, 9, -1,  -1, 5, -1,  -1, -1, -1],
        [-1, -1, -1,  2, -1, -1,  -1, -1, 5],
        [-1, -1, -1,  7, 1, 9,  -1, 8, -1],

        [-1, 5, -1,  -1, 6, 8,  -1, -1, -1],
        [2, -1, 6,  -1, -1, 3,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

        [5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [6, 7, -1,  1, -1, 5,  -1, 4, -1],
        [1, -1, 9,  -1, -1, -1,  2, -1, -1]
    ]

    # tells us if there is a solution
    print(solve_sudoku(example_board))

    # allows us to see the solution after the input is mutated
    print(example_board)