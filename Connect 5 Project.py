import numpy as np
import pygame
import sys

#Global variables are signified through all caps
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
    #Check if column isn't already filled
    return board[5][col] == 0

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

#Initialize pygame
pygame.init()

#Set size of each circle where a token can be dropped
CIRCLE_SIZE = 100
height = TOTAL_ROWS*CIRCLE_SIZE
width = TOTAL_COLUMNS*CIRCLE_SIZE

#Use Pygame documentation to determine method to use
size = (width, height)
screen = pygame.display.set_mode(size)


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if player == 0:
        col = int(input("Player 1, Selection (0-9):"))

        if is_valid_column(board,col):
            row = get_first_empty_row(board,col)
            drop_token(board, row, col, 1)

    else:
        col = int(input("Player 2, Selection (0-9):"))
        
        if is_valid_column(board,col):
            row = get_first_empty_row(board,col)
            drop_token(board, row, col, 2)

    print_board(board)
    
    player += 1
    player %= 2

    
