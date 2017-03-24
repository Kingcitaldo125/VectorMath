import pygame
import random
import math

pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
done = False

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

posx = winx/2
posy = winy/2
rad = 45
fill=0

circ_list = []
count = 0
total = 2

while not done:
    while count < total:
        ranx = random.randint(0,winx)
        rany = random.randint(0,winy)
        circ_list.append([ranx,rany])
        count+=1

    mPos = pygame.mouse.get_pos()

    for e in circ_list:
        if (math.sqrt((e[0]-mPos[0])**2 + (e[1]-mPos[1])**2) < rad):
            fill=1
        else:
            fill=0

    events = pygame.event.get()

    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True

    print(circ_list)
    screen.fill(black)
    for ic in circ_list:
        pygame.draw.circle(screen,red,(ic[0],ic[1]),rad,fill)

    pygame.display.flip()
pygame.display.quit()