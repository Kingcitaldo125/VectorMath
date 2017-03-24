import pygame
import random
import time

pygame.display.init()
winx = random.randrange(400,1000)
winy = random.randrange(300,800)

screen = pygame.display.set_mode((winx,winy))

num_cols = random.randrange(5,20)
num_rows = random.randrange(5,15)

white = (255,255,255)
black = (0,0,0)

width = winx/num_cols
height = winy/num_rows

recty=0
cur_row=1

#Draw the rows
while recty < winy:
    rectx=0
    if cur_row % 2==0:
        current = white
    else:
        current = black

    #Draw the cols
    while rectx < winx:
        pygame.draw.rect(screen,current,(rectx,recty,width,height))
        rectx+=width

        if current == white:
            current = black
        else:
            current = white

    recty+=height
    cur_row+=1

pygame.display.flip()
time.sleep(2)
pygame.display.quit()
