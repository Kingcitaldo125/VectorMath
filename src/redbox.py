# red box

import pygame
import time
import random

pygame.display.init()

winx = 800
winy = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
screen = pygame.display.set_mode((winx,winy))
done = False
currentcolor = red
width = 100
height = 50
collx = ((winx/2)-width/2)
colly = ((winy/2)-height/2)

while not done:
    events = pygame.event.get()
    mPos = pygame.mouse.get_pos()
    for e in events:
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True

    if mPos[0] > collx and mPos[0] <= (collx)+width:
        if mPos[1] > colly and mPos[1] < (colly)+height:
            currentcolor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    screen.fill(black)
    pygame.draw.rect(screen,currentcolor,(collx,colly,width,height),0)
    pygame.display.flip()

pygame.display.quit()