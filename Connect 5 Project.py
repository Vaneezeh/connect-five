import numpy as np
import pygame
import sys

#Global variables are signified through all caps
TOTAL_ROWS = 9
TOTAL_COLUMNS = 10

def create_board():
    board = np.zeros((TOTAL_ROWS,TOTAL_COLUMNS))
    return board

board = create_board()
#print_board(board)
game_over = False
player = 0

def drop_token(board, row, col, token):
    board[row][col] = token

def is_valid_column(board, col):
    #Check if column isn't already filled
    return board[TOTAL_ROWS - 1][col] == 0

def get_first_empty_row(board, col):
    for i in range(TOTAL_ROWS):
        if board[i][col] == 0:
            return i

def print_board(board):
    print(np.flip(board,0))

def won(board, token):
    #horizontal win
    for i in range (TOTAL_COLUMNS - 4):
        for j in range (TOTAL_ROWS):
            if board[j][i] == token and  board[j][i + 1] == token and board[j][i + 2] == token and board[j][i + 3] == token and board[j][i + 4] == token:
                return True
    #vertical win
    for i in range (TOTAL_COLUMNS):
        for j in range (TOTAL_ROWS -4):
            if board[j][i] == token and  board[j + 1][i] == token and board[j + 2][i] == token and board[j + 3][i] == token and board[j + 4][i] == token:
                return True
    #positive diagonal win
    for i in range (TOTAL_COLUMNS - 4):
        for j in range (TOTAL_ROWS -4):
            if board[j][i] == token and  board[j + 1][i + 1] == token and board[j + 2][i + 2] == token and board[j + 3][i + 3] == token and board[j + 4][i + 4] == token:
                return True
    #negative diagonal win
    for i in range (TOTAL_COLUMNS):
        for j in range (4, TOTAL_ROWS -4):
            if board[j][i] == token and  board[j - 1][i + 1] == token and board[j - 2][i + 2] == token and board[j - 3][i + 3] == token and board[j - 4][i + 4] == token:
                return True


#Initialize pygame
pygame.init()

#Set size of each circle where a token can be dropped
CIRCLE_SIZE = 100

#Creates a row for user to move piece along the top of the board
height = (TOTAL_ROWS+1)*CIRCLE_SIZE
width = TOTAL_COLUMNS*CIRCLE_SIZE

#Use Pygame documentation to determine method to use
size = (width, height)
screen = pygame.display.set_mode(size)

#Function to create GUI
def make_board(board):


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:

        if player == 0:
            col = int(input("Player 1, Selection (0-10):"))

            if is_valid_column(board,col):
                row = get_first_empty_row(board,col)
                drop_token(board, row, col, 1)

                if won(board, 1):
                    print("Player 1 wins")
                    game_over = True
                    break
        
        else:
            col = int(input("Player 2, Selection (0-10):"))
        
            if is_valid_column(board,col):
                row = get_first_empty_row(board,col)
                drop_token(board, row, col, 2)

                if won(board, 2):
                    print("Player 2 wins")
                    game_over = True
                    break
            

    print_board(board)
    
    player += 1
    player %= 2

    
