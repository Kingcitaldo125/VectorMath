import random
import pygame
import math
import time

red = (255,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
grey = (127,127,127)

def circle():
    color = grey#(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    rad = random.randrange(10,20)
    pos = [random.randrange(0,800-rad),random.randrange(0,600-rad)]
    circleobject = [color,pos,rad]
    return circleobject

def ring(pos):
    color = [255,0,0]
    rad = 2
    position = pos
    ringobject = [color,position,rad]
    return ringobject

winx = 800
winy = 600
pygame.display.init()
done = False
screen = pygame.display.set_mode((winx,winy))
clock = pygame.time.Clock()

numcircs = 0
circleList = []
ringlist = []
totalcircs = (random.randrange(2,20))

while numcircs < totalcircs:
    circleList.append(circle())
    numcircs+=1

radtotal = 0
for l in circleList:
    radtotal+=l[2]
    radavg = radtotal/numcircs

while not done:
    mPos = pygame.mouse.get_pos()

    #print(circleList)
    #Update
    dT = clock.tick() / 1000.0
    for cir in circleList:
        if( ( math.pow((mPos[0] - cir[1][0]),2) + math.pow(mPos[1] - cir[1][1],2))**0.5 <= cir[2]+1):
            ringlist.append(ring(cir[1]))

    for r in ringlist:
        if (r[0][1] and r[0][2] >= 255):
            ringlist.remove(r)
        if(r[2] > radavg):
            ringlist.remove(r)
            #print(r[0][0])
        r[0][1] += 350*dT
        r[0][2] += 350*dT
        #print(r[0][0])
        r[2] += 20*dT


    #Input
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True

    #Draw
    screen.fill(white)
    for ie in circleList:
        pygame.draw.circle(screen,black,ie[1],int(ie[2]+1))
        pygame.draw.circle(screen,ie[0],(ie[1]),ie[2])
    for r2 in ringlist:
        posx = int(r2[1][0])
        posy = int(r2[1][1])
        pygame.draw.circle(screen,r2[0],(posx,posy),int(r2[2]),1)
    pygame.display.flip()


pygame.display.quit()