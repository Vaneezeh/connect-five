import sys
import math
import numpy as np
import pygame


#Global variables are signified through all caps

BOARD_COLOUR = (84,255,159) 
HOLE_COLOUR = (255,225,255) 
P1_COLOUR = (255, 215, 0) 
P2_COLOUR = (131,111,255)

TOTAL_ROWS = 9
TOTAL_COLUMNS = 10

def create_board():
    """
    Creates a nested list of zeros with the dimensions of the nested list
    being TOTAL_ROWS by TOTAL_COLUMNS.

    Args:
        None

    Returns:
        None
    """
    board = np.zeros((TOTAL_ROWS,TOTAL_COLUMNS))
    return board

def drop_token(board, row, col, token):
    """
    Inserts a token (with values either a 1 or 2) into the given row and column indexes.

    Args:
        board: the game board, a nested list of zeros
        row (int): the row where the token will be inserted into
        col (int): the column where the token will be inserted into
        token (int): the token used to denote either player 1 or player 2

    Returns:
        None
        
    """
    board[row][col] = token

def is_valid_column(board, col): 
    """
    Returns a boolean stating whether or not the column is already filled to the top
    to prevent further insertion. 

    Args:
        board: the game board, a nested list of zeros
        col (int): the column where the token will be inserted into

    Returns:
        boolean
        
    """
    return board[TOTAL_ROWS - 1][col] == 0

def get_first_empty_row(board, col):
    """
    Returns an integer of the row where the token will be dropped
    for the chosen column. 

    Args:
        board: the game board, a nested list of zeros
        col (int): the column where the token will be inserted into

    Returns:
        int
        
    """
    for i in range(TOTAL_ROWS):
        if board[i][col] == 0:
            return i

def print_board(board):
    """
    Flips the board upside down to fix original numpy board appearance.

    Args:
        board: the game board, a nested list of zeros

    Returns:
        None
        
    """
    print(np.flip(board,0))

def won(board, token):
    """
    Returns a boolean as to whether or not either player achieved
    a win condition by forming one of the three possible token alignments:
    vertical, horizontal, diagonal.

    Args:
        board: the game board, a nested list of zeros
        token (int): the token used to denote either player 1 or player 2

    Returns:
        boolean
        
    """
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
    for i in range (TOTAL_COLUMNS -4):
        for j in range (4, TOTAL_ROWS -4):
            if board[j][i] == token and  board[j - 1][i + 1] == token and board[j - 2][i + 2] == token and board[j - 3][i + 3] == token and board[j - 4][i + 4] == token:
                return True

#Function to create GUI
def make_board(board):
    """
    Creates the GUI representation of the game board. 

    Args:
        board: the game board, a nested list of zeros

    Returns:
        None
        
    """
    for i in range (TOTAL_COLUMNS):
        for j in range (TOTAL_ROWS):
            pygame.draw.rect(screen, BOARD_COLOUR, (i*CIRCLE_SIZE, j*CIRCLE_SIZE+CIRCLE_SIZE, CIRCLE_SIZE, CIRCLE_SIZE))
            pygame.draw.circle(screen, HOLE_COLOUR, (int(i*CIRCLE_SIZE+CIRCLE_SIZE/2), int(j*CIRCLE_SIZE+CIRCLE_SIZE+CIRCLE_SIZE/2)), radius)
    for i in range(TOTAL_COLUMNS):
        for j in range(TOTAL_ROWS):
            if board[j][i] == 1:
                pygame.draw.circle(screen, P1_COLOUR, (int(i * CIRCLE_SIZE + CIRCLE_SIZE / 2), height - int(j * CIRCLE_SIZE + CIRCLE_SIZE / 2)), radius)
            elif board[j][i] == 2:
                pygame.draw.circle(screen, P2_COLOUR, (int(i * CIRCLE_SIZE + CIRCLE_SIZE / 2), height - int(j * CIRCLE_SIZE + CIRCLE_SIZE / 2)), radius)
    pygame.display.update()



board = create_board()
print_board(board)
game_over = False
player = 0

#Initialize pygame
pygame.init()

#Set size of each circle where a token can be dropped
CIRCLE_SIZE = 70

#Creates a row for user to move piece along the top of the board
height = (TOTAL_ROWS+1)*CIRCLE_SIZE
width = TOTAL_COLUMNS*CIRCLE_SIZE

#Use Pygame documentation to determine method to use
size = (width, height)
radius = int(CIRCLE_SIZE/2 - 10) #Subtract so it's smaller than the outer rectangle

screen = pygame.display.set_mode(size)
make_board(board)
pygame.display.update()

win_font = pygame.font.SysFont("Comic Sans MS", 75)

#Main Game Loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, HOLE_COLOUR, (0,0, width, CIRCLE_SIZE))
            position_x = event.pos[0]
            if player == 0:
                pygame.draw.circle(screen, P1_COLOUR, (position_x, int(CIRCLE_SIZE/2)), radius)
            else:
                pygame.draw.circle(screen, P2_COLOUR, (position_x, int(CIRCLE_SIZE/2)), radius)
        pygame.display.update()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, HOLE_COLOUR, (0,0, width, CIRCLE_SIZE))
            if player == 0:
                position_x = event.pos[0]
                col = int(math.floor(position_x/CIRCLE_SIZE))
                if is_valid_column(board,col):
                    row = get_first_empty_row(board,col)
                    drop_token(board, row, col, 1)

                    if won(board, 1):
                        win_message = win_font.render("Congratulations Player 1!", 1, P1_COLOUR)
                        screen.blit(win_message, (25,10))
                        print("Player 1 wins")
                        game_over = True
                        
            else:
                position_x = event.pos[0]
                col = int(math.floor(position_x / CIRCLE_SIZE))
                if is_valid_column(board,col):
                    row = get_first_empty_row(board,col)
                    drop_token(board, row, col, 2)

                    if won(board, 2):
                        win_message = win_font.render("Congratulations Player 2!", 1, P2_COLOUR)
                        screen.blit(win_message, (25,10))
                        print("Player 2 wins")
                        game_over = True
                        
            

            print_board(board)
            make_board(board)
    
            player += 1
            player %= 2

            if game_over:
                pygame.time.wait(10000)

    
