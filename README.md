# Connect Five
A game of Connect Five, coded in Python using the Pygame library

## Navigation

###### [Game Description](https://github.com/Vaneezeh/connect-five/blob/master/README.md#game-description-1)

###### [Gameplay](https://github.com/Vaneezeh/connect-five/blob/master/README.md#gameplay-1)

###### [Game Controls and Features](https://github.com/Vaneezeh/connect-five/blob/master/README.md#game-features-1)

###### [How to Install Connect Five](https://github.com/Vaneezeh/connect-five/blob/master/README.md#how-to-install-connect-five-1)

###### [Documentation](https://github.com/Vaneezeh/connect-five/blob/master/README.md#documentation-1)

###### [Authors](https://github.com/Vaneezeh/connect-five/blob/master/README.md#authors-1)

###### [Licensing Information](https://github.com/Vaneezeh/connect-five/blob/master/README.md#licensing-information-1)

## Game Description

Connect 5 requires two players for the game to operate. Player 1 starts off by dropping a token in an available column. Player 2 then drops a token in another available column. The two players interchange turns until one of the players gets 5 tokens in a row (the row can be in any direction, diagonals included). The game ends when a player got 5 tokens in a row, or both players have no more spots to drop a token in. The winner of the game is the first player to get to 5 tokens in a row first.

## Gameplay
![high rez ](https://user-images.githubusercontent.com/37009618/69932587-af310a80-1499-11ea-9b87-c7d5d258e0a8.gif)

<img width="573" alt="Screen Shot 2019-12-02 at 12 11 06 AM" src="https://user-images.githubusercontent.com/37009618/69932267-5dd44b80-1498-11ea-8c43-05d93e3742da.png">

## Game Controls and Features
All gameplay is controlled by mouse input. 

The game screen contains a 9 by 10 board.
* Use your mouse to hover over the column you wish to drop the token in. 
* Build 5 tokens in a row before your opponents does. 

The game will congratulate and automatically terminate once 5 tokens in a row of the same colour has been detected. 
## How to Install Connect Five

1) Go to https://github.com/Vaneezeh/connect-five 
2) Click on the green button on the right hand side which says ‘Clone or download’.
3) Download the zip file
4) Open Python and run the game

## Documentation

The documentation and directory structure of our project is located in our repository's Wiki page. You can find it [here](https://github.com/Vaneezeh/connect-five/wiki). 

## Authors 

This version of Connect Five was created by a group of statistics and computer science students at the University of Toronto Mississauga. This project was done for credit for the course, CSC290: Communication Skills for Computer Scientists. Group members as well as their individual contributions, are listed below: 

**Vaneezeh Siddiqui**

I was responsible for creating the GUI for this project. From developing the design before coding to implementing our team vision, my code contributions were primarily in the graphics department. I created both our design review and final presentation slides, so I was assigned a smaller amount of work for the README portion of this assignment. That being said, I set up the layout of the README on our Github page, handled the licensing, and wrote the section on how to extend the game. I also included a section detailing where users should look if they are looking to personalize our version of Connect Five. Finally, I looked over all the work for grammar and mechanics, and helped my teammates if needed.

**Nima Hashi**

I was put in charge of the won method and how the game would terminate if there was a winner or not. A case of their being no winner would only occur if the board is completely full and neither of the two players got 5 tokens in a row. The won function plays a big part in the games functionality and the game depends greatly on it. I also made a section that includes instructions on how users should install Connect 5 and how to play the game. I included screenshots to clearly show where the users should go and what they should do incase they do have any trouble following my instructions. Lastly, I made a section describing a project directory structure for the users who choose to enhance our code. This section will help them understand what our functions and classes are used for. Throughout the project, my teammates and I all took part in helping each other and taking responsibility when needed since we were down a member.

**Charles Jacob Tan**

Throughout this game's development process, I was fundamentally in charge of implementing the structure of the game and cleaning up any residual bugs and issues that were left from my teammates whether it be minimal or substantial. This also includes ensuring that our different coding styles meshed well together and exhibited strong signs of consistency. I had to  finally verify that each one of us executed proper code practices and that there would be a good semblance of code clarity after every subsequent commit. Once the game was fully functional and the coding stages were complete, I was responsible for adding doc strings to the main functions of the game. Within the README file, I was in charge of both the "Gameplay" and "Game Controls and Features" sections. I also edited the wiki by adding to the "Directory Structure" section and stating a few more details to the "How to extend the game" options. 

## Licensing Information

Connect Five is licensed under the MIT License (MIT)

Copyright © 2019 Connect Five

You can find a copy of the License at https://opensource.org/licenses/MIT

