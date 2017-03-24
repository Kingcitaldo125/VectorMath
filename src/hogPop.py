radius = 20
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
teal = (0,255,255)
green = (0,255,0)

totalScore = 0

def selectHog():
    """ """
    x = random.randint(radius,winx-radius)
    y = random.randint(radius,winy-radius)
    hogList.append([x,y])

def drawHog(surf,xx,yy):
    """ """
    colorSelect = random.randint(0,4)
    if colorSelect == 0:
        chosen = red
    elif colorSelect == 1:
        chosen = blue
    elif colorSelect == 2:
        chosen = teal
    elif colorSelect == 3:
        chosen = green
    else:
        chosen = white
    if chosen == white:
        pygame.draw.circle(surf,chosen,(int(xx),int(yy)),radius,1)
    else:
        pygame.draw.circle(surf,chosen,(int(xx),int(yy)),radius)

def doClickDetection(mpm):
    """ """
    for element in hogList:
        if((math.pow((element[0] - mpm[0]),2) + math.pow((element[1] - mpm[1]),2))**0.5 <= radius+1):
            #print("IN RANGE")
            if mClick == (1,0,0):
                hogList.remove(element)

import pygame
import random
import math

winx = 800
winy = 600

pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((winx,winy))

hogList = []
selectHog()
done = False

while not done:
    mPos = pygame.mouse.get_pos()
    mClick = pygame.mouse.get_pressed()
    if hogList.__len__ == 0:
        print("ZERO")
    #for ea in hogList:
        #print(ea)
    element = hogList[0]

    if((math.pow((element[0] - mPos[0]),2) + math.pow((element[1] - mPos[1]),2))**0.5 <= radius+1):
        #print("IN RANGE")
        if mClick == (1,0,0):
            totalScore+=1
            hogList.remove(element)
            selectHog()
                
    events = pygame.event.get()
    for et in events:
        if et.type == pygame.KEYDOWN:
            if et.key == pygame.K_ESCAPE:
                done = True

    screen.fill(black)
    #print(hogList[0][1])
    drawHog(screen,hogList[0][0],hogList[0][1])
    pygame.display.flip()

pygame.display.quit()

