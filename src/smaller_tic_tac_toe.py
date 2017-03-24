def showBoard (ttt, board):
# (re)draw the game board (board) on the screen (ttt)
    ttt.blit (board, (0,0))

def initboard(ttt):
     background = pygame.Surface (ttt.get_size())
     background = background.convert()

     background.fill ((169,169,169))

# draw the grid lines

# vertical lines...

     pygame.draw.line (background, (0,0,0), (100,0), (100,300), 2)

     pygame.draw.line (background, (0,0,0), (200,0), (200,300), 2)

# horizontal lines...

     pygame.draw.line (background, (0,0,0), (0,100), (300,100), 2)

     pygame.draw.line (background, (0,0,0), (0,200), (300,200), 2)

# return the board
     return background

def boardPos (mx, my):
# determine the row the user clicked
    if (my < 100):

        row = 0
    elif (my < 200):
        row = 1
    else:
        row = 2

# determine the column the user clicked
    if (mx < 100):

        col = 0
    elif (mx < 200):
        col = 1
    else:
        col = 2
#return the row & column
    return (row, col)

def handleInput(self, offsetx, offsety):
        """Handles all input"""
        eList = pygame.event.get()
        mousePressed = pygame.mouse.get_pressed()
        for e in eList:
            if e.type == mousePressed and e.button == (1,0,0):
                if self.state == str("Normal"):
                    drawObject()
                    self.cur_player = 0
                elif self.state == str("Normal") and self.cur_player == 0:
                    drawObject()
                    self.cur_player = 1
                else:
                    return True
def drawMove (board, boardRow, boardCol, Piece):
# draw an X or O (Piece) on the board at boardRow, boardCol
# determine the center of the space

# (this works because our spaces are 100 pixels wide and the first one

#  is numbered zero)

    centerX = boardCol * 100 + 50

    centerY = boardRow * 100 + 50

# draw the piece

    if (Piece == "O"):

# it's an O; draw a circle
        pygame.draw.circle (board, (0,0,0), (centerX, centerY), 44, 2)

    else:
# it's an X
        pygame.draw.line (board, (0,0,0), (centerX - 22, centerY - 22), \
        (centerX + 22, centerY + 22), 2)
        pygame.draw.line (board, (0,0,0), (centerX + 22, centerY - 22), \
        (centerX - 22, centerY + 22), 2)
# mark the board space as used
        grid[boardRow][boardCol] = Piece
def clickBoard (board):
# determine where the user clicked on the board and draw the X or O
# tell Python that we want access to the global variables grid & XO
    global grid, XO

    (mouseX, mouseY) = pygame.mouse.get_pos()

    (row, col) = boardPos (mouseX, mouseY)



# make sure this space isn't used
    if ((grid[row][col] == "X") or (grid[row][col] == "O")):

# this space is in use
        return

# draw an X or O
    drawMove (board, row, col, XO)

# toggle XO to the other player's move
    if (XO == "X"):

        XO = "O"
    else:
        XO = "X"
def drawStatus (board):
# draw the status (i.e., player turn, etc) at the bottom of the board
# --------------------------------

# board : the initialized game board surface

# gain access to global variables

global XO, winner

Now that we have declared our function and have access to the global variables, we need to figure out what status message we're going to draw. There are two possible types of messages: the ``you won'' message and the ``someone's turn'' message. We'll determine the appropriate messsage with an if statement, and store the message in the variable message.
# determine the status message
if (winner is None):

message = XO + "'s turn"
else:
message = winner + " won!"
Now that we have the status message we need to display it on the game board. PyGame has three steps for displaying text on a surface. First, get the font you're working with. Second, render the text onto a new surface. Finally, copy (blit) that surface onto your destination surface. We'll accomplish that with the following code.
# render the status message
font = pygame.font.Font(None, 24)

text = font.render(message, 1, (0,0,0))

# copy the rendered message onto the board

board.fill ((250, 250, 250), (0, 300, 300, 25))
board.blit (text, (10, 300))

import pygame

from pygame.locals import *

pygame.display.init()

pygame.font.init()

ttt = pygame.display.set_mode((300,325))

pygame.display.set_caption = ('Tic-Tac-Toe')

done = False

board = initboard (ttt)

pygame.event.get()

mx, my = pygame.mouse.get_pos()
#Game Loops

while not done:
    #UPDATE#

    #INPUT#
    handleInput()

    #DRAW#
    initboard(ttt)
    showBoard(ttt,board)
    pygame.display.flip()

pygame.font.quit()
pygame.display.quit()
