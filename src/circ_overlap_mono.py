import pygame
import time
import math
import random

pygame.display.init()
clock=pygame.time.Clock()
winx = 300
winy = 150
screen = pygame.display.set_mode((winx,winy))
circ1x = random.randrange(0,winx)
circ1y = random.randrange(0,winy)
rad1 = 20

circ2x = int(winx/2)
circ2y =  int(winy/2)
rad2 = 20
red = (255,0,0)
blue = (100,55,200)
black = (0,0,0)
hit = False
done = False
secs = 0

while not done:
#IF THE DISTANCE BETWEEN BOTH BODIES < THE SUM OF THE RADII OF BOTH BODIES: HIT
    dT = clock.tick() / 1000.0
    secs +=1*dT
    if secs >= 3.0:
        screen.fill(black)
        circ1x = random.randrange(0,winx)
        circ1y = random.randrange(0,winy)
        secs = 0
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
    if math.sqrt( (abs(circ2x - circ1x) )**2 + (abs(circ2y-circ1y))**2) <= (rad1+rad2):
        hit = True
    else:
        hit = False

    if hit == True:
        pygame.draw.circle(screen,red,(circ1x,circ1y),rad1,1)
        pygame.draw.circle(screen,blue,(circ2x,circ2y),rad2,1)
    else:
        pygame.draw.circle(screen,red,(circ1x,circ1y),rad1,0)
        pygame.draw.circle(screen,blue,(circ2x,circ2y),rad2,0)


    pygame.display.flip()
#time.sleep(1.89)
pygame.display.quit()