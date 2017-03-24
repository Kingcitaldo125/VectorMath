import pygame
import math
import time
import random

ranposx = random.randrange(25,750)
ranposy = random.randrange(25,585)

def newski(ranx,rany):
    skiobject = [ranx,rany]
    return skiobject

winx = 800
winy = 600
pygame.display.init()

screen = pygame.display.set_mode((winx,winy))
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
rad = 25
clock = pygame.time.Clock()

done = False
skilist = []
velocity = [[0.0,0.0]]
theta = 0
friction = 0.00001
skilist.append(newski(ranposx,ranposy))
while not done:
    #Update
    dT = clock.tick() / 1000.0

    for vobject in velocity:
        #print(vobject)
        if(vobject[0] > 0.0):
            vobject[0] -= friction
        if(vobject[0] < 0.0):
            vobject[0] += friction
        if(vobject[1] > 0.0):
            vobject[1] -= friction
        if(vobject[1] < 0.0):
            vobject[1] += friction

    for s in skilist:
        position_vector = [[s[0]+velocity[0][0],s[1]+velocity[0][1]]]
        if(s[0] > winx-rad):
            s[0] = (winx + rad) - s[0]

        if(s[1] > winy-rad):
            s[1] = (winy + rad) - s[1]

        if(s[0] < rad):
            s[0] = (winx - rad) - s[0]

        if(s[1] < rad):
            s[1] = (winy - rad) - s[1]

        s[0]+=velocity[0][0]
        s[1]+=velocity[0][1]

    #input
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
            if e.key == pygame.K_w:
                for ie in velocity:
                    ie[1]-=0.1
            if e.key == pygame.K_a:
                for ii in velocity:
                    ii[0]-=0.1
            if e.key == pygame.K_d:
                for nie in velocity:
                    nie[0]+=0.1
            if e.key == pygame.K_s:
                for m in velocity:
                    m[1]+=0.1

    screen.fill(black)
    for ski in skilist:
        position_vector = [ [ ski[0]+velocity[0][0]*10,ski[1]+velocity[0][1]*10 ] ]
        pygame.draw.circle(screen,red,(int(ski[0]),int(ski[1])),rad)
        pygame.draw.line(screen,red,ski,(position_vector[0][0],position_vector[0][1]))
    pygame.display.flip()
pygame.display.quit()