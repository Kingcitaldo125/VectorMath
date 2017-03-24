import pygame
import random
import math

pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
done = False

clockObject = pygame.time.Clock()
enemyspeed = 140
enemyRad = 10
nums = 0
timer1 = 0.0
white = (255,255,255)
black = (0,0,0)
create = False
E = []

def appendEnemies():
    """ """
    E.append([random.randrange(-100,0),random.randrange(0,winy)])

def number_enemies():
    """Returns the number of enemies"""
    return nums

def Drawenemy(surf):
    """Draws all enemies """
    for ie in E:
        pygame.draw.circle(surf, white, (int(ie[0]),int(ie[1])), enemyRad)

def update():
    """Will advance enemy x pos"""
    for ee in E:
        if(ee[0] >= winx):
            E.remove(ee)
        ee[0]+=enemyspeed*dT


while not done:
    # UPDATE #
    x = 1
    y = random.randint(1,599)
    dT = clockObject.tick() / 1000
    update()

    # INPUT #
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                appendEnemies()
            if e.key == pygame.K_ESCAPE:
                done = True

    # DRAW #
    screen.fill(black)
    print(E)
    Drawenemy(screen)
    pygame.display.flip()
pygame.display.quit()
