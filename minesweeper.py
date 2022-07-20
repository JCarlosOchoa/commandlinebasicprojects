import random

import re


# we must create a board object to represent our minesweeper game
# this is so we can say "create a new board object", or 
# "dig here," or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # we will keep track of the params since they'll be useful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create a board
        # helper functions
        self.board = self.make_new_board() # we need to plant the bombs
        self.assign_values_to_board() # we can assign values to cells representing the number of adjacent bombs

        # initializing a set to keep track of which locations have been uncovered
        # (row, col) tuples will be saved here
        self.dug = set() # if we dig at (0,0), then self.dug = {(0,0)}
    
    def make_new_board(self):
        # construct a new board based on the dim_size and num_bombs
        # we should construct the list of lists here since it is a 2-D board
        
        # generate a new board
        # square board: dim_size x dim_size with each cell containing None
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            # each cell given an unique id
            loc = random.randint(0, self.dim_size** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == "*":
                # there is already a bomb at loc. don't incrememnt bombs_planted
                continue

            board[row][col] = "*"
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # now that we have bombs planted, let's assign a number
        # 0-8 for all the empty spaces, which represents the number of adjacent
        # bombs there are. we compute this BEFORE starting gameplay to 
        # save some effort in having to check each cell later on
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue

                # helper function to help count the bombs
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
            
    def get_num_neighboring_bombs(self, row, col):
        # to count the neighboring bombs:
        # iterate through each of the neighboring positions and sum the number of bombs
        # top left: (row-1, col-1)
        # top middle: (row, col-1)
        # top left: (row + 1, col + 1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure we don't go out of bounds
        num_neighboring_bombs = 0

        for r in range(max(0, row - 1), min(self.dim_size-1, (row + 1)) +1):
            for c in range(max(0, col-1), min(self.dim_size - 1, (col+1)) +1):
                if r == row and c == col:
                    #this is the dug up cell, don't check
                    continue
                if self.board[r][c] == "*":
                    num_neighboring_bombs += 1
                
        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at the user-chosen location
        # return True if successful dig, False if bomb dug
        self.dug.add((row, col))

        # hit a bomb -> game over
        if self.board[row][col] == "*":
            return False
        
        # dig at location with neighboring bombs -> finish dig
        elif self.board[row][col] > 0:
            return True

        # dig at location with no neighboring bombs -> recursively dig neighbors
        # self.board[row][col] == 0
        for r in range(max(0, row - 1), min(self.dim_size-1, (row + 1)) +1):
            for c in range(max(0, col-1), min(self.dim_size - 1, (col+1)) +1):
                if (r,c) in self.dug:
                    continue # don't dig where you've already dug

                self.dig(r, c)
        
        # if our initial dig didn't hit a bomb, that means that none of the above interations would hit a bomb
        # this means that there's no way we should hit a bomb out here since we'd stop somewhere adjacent to a bomb
        return True
        
    def __str__(self):
        # function that when you call print on this object
        # it'll print out whatever this function returns
        # OUTPUT: return a string that shows the board to the player
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "
        
        # put this together in a string
        string_rep = ""

        # get max column width for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = "    "
        cells = []
        for idx, col in enumerate(indices):
            format = "%-" + str(widths[idx]) + "s"
            cells.append(format % (col))

        indices_row += "   ".join(cells)
        indices_row += "   \n"

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f"{i} |"
            cells = []
            for idx, col in enumerate(row):
                format = "%-" + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += "  |".join(cells)
            string_rep += "  |\n"
        
        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + "-"*str_len + "\n" + string_rep + "-"*str_len

        return string_rep

# Play the game
def play(dim_size=10, num_bombs=10):
    # step 1: Create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # step 2: show user the board and ask for where they want to dig
    

    # step 3a: if location is a bomb, show GAME OVER messge
    # step 3b: if location is not a bomb, dig recursively until each square
    #  is at least next to a bomb
    # step 4: repeat steps 2 and 3a/b until there are no more places to dig --> VICTORY
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)

        # the regex allows us to handle any user input
        user_input = re.split(",(\\s)*", input("Where would you like to dig? Input as row,col: ")) # "0, 3"

        row, col = int(user_input[0]), int(user_input[-1])

        # if out of bounds, try again
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location. Try again.")
            continue
        
        # if valid input, we dig
        # value is True/False
        safe  = board.dig(row, col)

        if not safe:
            # dug a bomb
            break # GAME OVER

    # 2 ways to end loop
    if safe: # all spaces have been dug safely
        print("YOU WIN!")
    else:
        print("SORRY, YOU LOSE!")

        #reveal the board once you lose
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == "__main__": # good practice
    play()