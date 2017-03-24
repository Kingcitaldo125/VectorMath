import pygame
import tictactoe

pygame.display.init()
pygame.font.init()
win_width = 600
win_height = 660
leftx = 10
topy = 10
screen = pygame.display.set_mode((win_width,win_height))
done = False
game = tictactoe.Board((580, 610), 30) #Dims for the game board

while not done:
    # UPDATE
    # Empty -- this game is all input-driven!

    # INPUT
    done = game.handleInput(leftx, topy)

    # DRAW
    game.render()
    screen.fill((150,150,150))
    screen.blit(game.surf, (leftx, topy))
    pygame.display.flip()

pygame.font.quit()
pygame.display.quit()
