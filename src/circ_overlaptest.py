import math
import random
import pygame

pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
done = False
clock = pygame.time.Clock()

myCircles = []
hitCircles = []
curnum = 0
myrad1 = 20
myrad2 = myrad1

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
blue = (100,55,250)
hit = False
secs = 0
hits = []
nohits = []

while not done:
    total = random.randrange(5,100)
    dT = clock.tick() / 1000.0
    mPos = pygame.mouse.get_pos()
    mx = mPos[0]
    my = mPos[1]

    while curnum < total:
        ranx = random.randint(myrad1,winx-myrad1)
        rany = random.randint(myrad2,winy-myrad2)
        myCircles.append([ranx,rany])
        curnum+=1
    secs+=1*dT
    print(secs)
    if secs > 5:
        curnum = 0
        secs=0
        myCircles = []
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True

    screen.fill(black)
    for i in myCircles:
        for ii in myCircles:
            if i != ii:
                if math.sqrt( (abs(i[0] - ii[0])**2) + (abs(i[1] - ii[1])**2)) < (myrad1+myrad2):
                    pygame.draw.circle(screen,white,(int(i[0]),int(i[1])),myrad1,0)
                else:
                    pygame.draw.circle(screen,blue,(int(i[0]),int(i[1])),myrad1,1)

    pygame.display.flip()
pygame.display.quit()