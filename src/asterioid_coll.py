import pygame
import time
import random

winx = 800
winy = 600
pygame.display.init()
screen = pygame.display.set_mode((winx,winy))
done = False
clock = pygame.time.Clock()
asteroids = []
astrad = 25
blue = (0,0,255)
red = (255,0,0)
black = (0,0,0)
speed = 200
randirec = random.randint(0,3)
timermax = 4
timercur = 0

while not done:
    #Update
    dT = clock.tick() / 1000.0
    for ex in asteroids:
        if ex[0] > winx and ex[1] > winy:
            asteroids.remove(ex)
        elif ex[0] > winx:
            asteroids.remove(ex)
        elif ex[1] > winy:
            asteroids.remove(ex)
        elif ex[0] < 0:
            asteroids.remove(ex)
        elif ex[0] < 0 and ex[1] < 0:
            asteroids.remove(ex)
        else:
            if randirec == 0:
                ex[0]+=speed*dT
            elif randirec == 1:
                ex[0]-=speed*dT
            elif randirec == 2:
                ex[1]+=speed*dT
            else:
                ex[1]-=speed*dT

    #input
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
            if e.key == pygame.K_SPACE:
                ranx = random.randrange(1,winx-1)
                rany = random.randrange(1,winy-1)
                asteroids.append([ranx,rany])

    screen.fill(black)
    pygame.draw.circle(screen,blue,(400,300),5)
    for i in asteroids:
        pygame.draw.circle(screen,red,(int(i[0]),int(i[1])),astrad)


    #print(asteroids)
    pygame.display.flip()
pygame.display.quit()