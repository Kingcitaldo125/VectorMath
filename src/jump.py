import pygame
import math
import random

pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
done = False
clock = pygame.time.Clock()
circlerad = 30
cx = 400
cy = 300
horzvel = [0]
red = (255,0,0)
black = (0,0,0)
teal = (0,255,255)
a=0.5 #Where a is the speed multiplier??\
movement = [10,10] #pixels
jumpstate = False
gravity = 100


while not done:
    #Update
    readyPos = winy-circlerad

    if cy >= readyPos:
        jumpstate = False

    if cx-circlerad < 0:
        cx = circlerad

    if cx+circlerad > winx:
        cx = winx-circlerad

    if cy+circlerad >= winy:
        #print(cy)
        a = 0
        jumpstate=False

    dT = clock.tick() / 1000.0

    cx+=horzvel[0]

    if jumpstate:
        a=-500
        velocity=a*dT
        cy+=velocity
        jumpstate=False
    else:
        velocity = a*dT
        cy+=velocity
    if jumpstate==False:
        a+=1
    else:
        a-=1

    #print(velocity)

    event = pygame.event.get()
    mPress = pygame.mouse.get_pressed()
    mPos = pygame.mouse.get_pos()
    circlePos = (cx,cy)
    sub1 = abs(cy - mPos[1])
    sub2 = abs(cx - mPos[0])
    radsum = circlerad+1
    #print(mPos[0])
    if math.sqrt(sub1**2 + sub2**2) <= radsum:
        for eee in event:
            if eee.type == pygame.MOUSEBUTTONDOWN:
                curCol = teal
    else:
        curCol = red

    for e in event:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                cx+=movement[0]

            if e.key == pygame.K_a:
                cx-=movement[0]

            if e.key == pygame.K_SPACE:
                if jumpstate:
                    continue
                #print(a)
                cy=winy-(circlerad*2)
                jumpstate=True
            if e.key == pygame.K_ESCAPE:
                done=True

    screen.fill(black)
    print(cx)
    pygame.draw.circle(screen,curCol,(int(cx),int(cy)),circlerad)
    pygame.display.flip()


pygame.display.quit()