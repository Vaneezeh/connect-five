import numpy as np

TOTAL_ROWS = 9
TOTAL_COLUMNS = 10

def create_board():
    board = np.zeros((9,10))
    return board

board = create_board()
#print_board(board)
game_over = False
player = 0

def drop_token(board, row, col, token):
    board[row][col] = token

def is_valid_column(board, col):
    return board[5][col] == 0 #checks that the row is not already filled to the top

def get_first_empty_row(board, col):
    for i in range(TOTAL_ROWS):
        if board[i][col] == 0:
            return i

def print_board(board):
    print(np.flip(board,0))

def won(board, token):
    for i in range (TOTAL_COLUMNS - 3):
        for j in range (TOTAL_ROWS):
            if board[i][j] == token and  board[i][j + 1] == token and board[i][j + 2] == token and board[i][j + 3] == token:
                return True
    for i in range (TOTAL_COLUMNS):
        for j in range (TOTAL_ROWS - 3):
            if board[i][j] == token and  board[i][j + 1] == token and board[i][j + 2] == token and board[i][j + 3] == token:
                return True
    for i in range (TOTAL_COLUMNS - 3):
        for j in range (TOTAL_ROWS - 3):
            if board[i][j] == token and  board[i + 1][j + 1] == token and board[i + 1][j + 2] == token and board[i + 3][j + 3] == token:
                return True
    for i in range (TOTAL_COLUMNS - 3):
        for j in range (TOTAL_ROWS - 3):
            if board[i][j] == token and  board[i + 1][j + 1] == token and board[i + 1][j + 2] == token and board[i + 3][j + 3] == token:
                return True
    return False
            
            
while not game_over:
    if player == 0:
        col = int(input("Player 1, Selection (0-6):"))

        if is_valid_column(board,col):
            row = get_first_empty_row(board,col)
            drop_token(board, row, col, 1)

    else:
        col = int(input("Player 2, Selection (0-6):"))
        
        if is_valid_column(board,col):
            row = get_first_empty_row(board,col)
            drop_token(board, row, col, 2)

    print_board(board)
    
    player += 1
    player %= 2

    
