class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] #the index of this list will represent a 3x3 board
        self.current_winner = None # keep track of winner!

    def print_board(self):
        # the board has indeces 0 - 8. each i would refer to indeces 0-2, 3-5, 6-8, which are the rows of length 3
        for row in [self.board[i*3: (i+1) * 3] for i in range(3)]:
            print ("| " + " | ".join(row) + " |")
    
    @staticmethod # static method bc it does not refer to any specific board, meaning we don't have to pass in self
    def print_board_nums():
        # 0 | 1 | 2, etc -- tells us what number corresponds to which box
        # an array containing arrays. j counts each subarray. i will populate each subarray with the numbers
        number_board = [ [str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print ("| " + " | ".join(row) + " |")
    
    def available_moves(self):
        # list comprehension of below loop
        return [i for (i, spot) in enumerate(self.board) if spot == " "]

        # elongated iteration
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # enumerate makes a list of tuples (index, value at index)
        #     # row in board may look like [x, x, o] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot = " ":
        #         moves.append(i)
        # return moves