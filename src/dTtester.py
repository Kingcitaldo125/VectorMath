import pygame
import time
import random

pygame.display.init()
winx = 800
winy = 300
#screen = pygame.display.set_mode((winx,winy))
done = False
clock = pygame.time.Clock()

secs = 0
speed = 1
rad = 5
red = (255,0,0)

myList = []
while not done:
    #update
    screen = pygame.display.set_mode((winx,winy))
    dT = clock.tick() / 1000.0
        #secs+=int(speed)
    secs+=speed*dT
    #Input
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                winx-=10
                winy-=10
            if e.key == pygame.K_ESCAPE:
                done = True
        if e.type == pygame.MOUSEMOTION:
            #print(e.type)
            if e.type == pygame.MOUSEMOTION:
                winx+=1
                winy+=1
            ranx = random.randrange(0,winx)
            rany = random.randrange(0,winy)
            myList.append([ranx,rany])


    #Draw stuff
    screen.fill((0,0,0))
    for e in myList:
        pygame.draw.circle(screen,red,(e[0],e[1]),rad)

    pygame.display.flip()
pygame.display.quit()