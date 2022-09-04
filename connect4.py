import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(Board, row, col, piece):
    Board[row][col] = piece

def is_valid_location(Board, col):
    return Board[ROW_COUNT-1][col] == 0

def get_next_open_row(Board, col):
    for r in range(ROW_COUNT):
        if Board[r][col] == 0:
            return r

def print_board(Board):
    print(np.flip(Board,0))

def winning_move(Board, piece):
    # check horizontal locations for win 
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if Board[r][c] == piece and Board[r][c+1] == piece and  Board[r][c+2] == piece and Board[r][c+3] == piece:
                return True

     # check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if Board[r][c] == piece and Board[r+1][c] == piece and  Board[r+2][c] == piece and Board[r+3][c] == piece:
                return True
    
    # check for the positively sloped diagonals


    # check for the negatively sloped diagonals


Board = create_board()
print_board(Board)
game_over = False
turn = 0

while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = int(input('Player 1 make your selection (0-6):'))
        if is_valid_location(Board, col):
            row = get_next_open_row(Board, col)
            drop_piece(Board, row, col, 1)
            
            if winning_move(Board, 1):
                print('Player 1 wins')
                game_over = True

    #Ask for player 2 input
    else:
        col = int(input('Player 2 make your selection (0-6):'))
        if is_valid_location(Board, col):
            row = get_next_open_row(Board, col)
            drop_piece(Board, row, col, 2)
    print_board(Board)    
    turn += 1
    turn = turn % 2

