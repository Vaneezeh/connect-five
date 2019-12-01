# Connect Five
A game of Connect Five, coded in Python using the Pygame library

## Navigation

###### [Game Description](https://github.com/Vaneezeh/connect-five/blob/master/README.md#game-description-1)

###### [Game Features](https://github.com/Vaneezeh/connect-five/blob/master/README.md#game-features-1)

###### [How to Install Connect Five](https://github.com/Vaneezeh/connect-five/blob/master/README.md#how-to-install-connect-five-1)

###### [Documentation](https://github.com/Vaneezeh/connect-five/blob/master/README.md#documentation-1)

###### [Authors](https://github.com/Vaneezeh/connect-five/blob/master/README.md#authors-1)

###### [Licensing Information](https://github.com/Vaneezeh/connect-five/blob/master/README.md#licensing-information-1)

## Game Description

Connect 5 requires two players for the game to operate. Player 1 starts off by dropping a token in an available column. Player 2 then drops a token in another available column. The two players interchange turns until one of the players gets 5 tokens in a row (the row can be in any direction, diagonals included). The game ends when a player got 5 tokens in a row, or both players have no more spots to drop a token in. The winner of the game is the first player to get to 5 tokens in a row first.

## Game Features

## How to Install Connect Five

1) Go to https://github.com/Vaneezeh/connect-five 
2) Click on the green button on the right hand side which says ‘Clone or download’.
3) Download the zip file
4) Open Python and run the game

## Documentation

Below you'll see the documnenation of all the methods used in Connect 5.

def create_board():
  Creates the board (9x10 grid) for the players to play on. 
   
def drop_token(board, row, col, token):
  Drop the token at the row and col position the player chooses.
  
def is_valid_column(board, col):
  Check to see if the spot the player chose is empty or not.
   
def get_first_empty_row(board, col):
  Return the digit of the first empty row in the col the player chose to drop their token.

def print_board(board):
  Print the board at its current position.
 
def won(board, token):
  Checks to see if the player has 5 tokens in a row or not.

Main:
  While there is still empty spots for the players to drop their tokens in, we manually switch the players turn between the     two, starting with player 1. Whenever a player drops a token in a column, we check to see if they got 5 tokens in a row, if   so then that player won the game and we end it. If not, then we switch to the next players turn until we get to a spot where   there is a winner or there are no moves left.

## Authors 

This version of Connect Five was created by a group of statistics and computer science students at the University of Toronto Mississauga. This project was done for credit for the course, CSC290: Communication Skills for Computer Scientists. Group members as well as their individual contributions, are listed below: 

**Vaneezeh Siddiqui**

I was responsible for creating the GUI for this project. From developing the design before coding to implementing our team vision, my code contributions were primarily in the graphics department. I created both our design review and final presentation slides, so I was assigned a smaller amount of work for the README portion of this assignment. That being said, I set up the layout of the README on our Github page, handled the licensing, and wrote the section on how to extend the game. I also included a section detailing where users should look if they are looking to personalize our version of Connect Five. Finally, I looked over all the work for grammar and mechanics, and helped my teammates if needed.

**Nima Hashi**

I was put in charge of the won method and how the game would terminate if there was a winner or not. A case of their being no winner would only occur if the board is completely full and neither of the two players got 5 tokens in a row. The won function plays a big part in the games functionality and the game depends greatly on it. I also made a section that includes instructions on how users should install Connect 5 and how to play the game. I included screenshots to clearly show where the users should go and what they should do incase they do have any trouble following my instructions. Lastly, I made a section describing a project directory structure for the users who choose to enhance our code. This section will help them understand what our functions and classes are used for. Throughout the project, my teammates and I all took part in helping each other and taking responsibility when needed since we were down a member.

**Charles Jacob Tan**

Throughout this game's development process, I was fundamentally in charge of implementing the structure of the game and cleaning up any residual bugs and issues that were left from my teammates whether it be minimal or substantial. This also includes ensuring that our different coding styles meshed well together and exhibited strong signs of consistency. I had to  finally verify that each one of us executed proper code practices and that there would be a good semblance of code clarity after every subsequent commit. Once the game was fully functional and the coding stages were complete, I was responsible for adding doc strings to the main functions of the game. Within the README file, I edited the wiki by adding to the "Directory Structure" section and stating a few more details to the "How to extend the game" options. 

## Licensing Information

Connect Five is licensed under the MIT License (MIT)

Copyright © 2019 Connect Five

You can find a copy of the License at https://opensource.org/licenses/MIT

