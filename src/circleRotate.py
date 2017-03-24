import pygame
import time
import math

pygame.display.init()

winx = 800
winy = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

done = False
clock = pygame.time.Clock()

screen = pygame.display.set_mode((winx,winy))

radius = 100

theta = 1.0
speed=1
xrot=0
yrot=0
chosencolor=white

while not done:
    dT = clock.tick() / 1000.0
    events = pygame.event.get()
    mPos = pygame.mouse.get_pos()
    
    xrot = radius*math.cos(theta) - radius*math.sin(theta)
    yrot = radius*math.sin(theta) + radius*math.cos(theta)
    theta+=speed*dT

    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
        if e.type == pygame.QUIT:
            done = True

    screen.fill(black)
    xrot+=400
    yrot+=300
    if(math.sqrt((mPos[0]-xrot)**2 + (mPos[1]-yrot)**2 )<=21):
        chosencolor=red
    else:
        chosencolor=white
    pygame.draw.circle(screen,chosencolor,(int(xrot),int(yrot)),20)

    pygame.display.flip()

pygame.display.quit()
