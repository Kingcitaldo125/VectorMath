import pygame
import random
import time


pygame.display.init()
screen = pygame.display.set_mode((800,600))

done = False

while done != True:
    # @@@@@@ #
    # Update #
    # @@@@@@ #
    circx = 400
    circy = 300
    r = 255
    b = 0
    g = 0
    radius = 15

    # @@@@@ #
    # Input #
    # @@@@@ #
    pygame.event.get()
    keyPresses = pygame.key.get_pressed()
    mousePresses = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    if keyPresses[pygame.K_ESCAPE]:
        done = True

    # @@@@ #
    # Draw #
    # @@@@ #
    if mousePresses == (1,0,0):
        pygame.draw.circle(screen, (r,g,b), (mx,my),radius)
    #print(mousePresses)




    pygame.display.flip()
if done == True:
    pygame.display.quit()