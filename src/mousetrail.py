import time
import pygame
import random

pygame.display.init()
winx = 800
winy = 600

screen = pygame.display.set_mode((winx,winy))
circList = []
clock = pygame.time.Clock()
red = (255,0,0)
red_val = 255
black = (0,0,0)
done = False
rad = 30
count = 0.0
inverse_count = red_val

while not done:
    dT = clock.tick() / 1000.0
    if red_val > 0:
        red_val -= 15*dT
    count += 8*dT
    inverse_count -= 1*dT
    if count > 0.65:
        count = 0.0
        circList.append((mPos,red_val))

    mPos = pygame.mouse.get_pos()
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True

    screen.fill(black)
    pygame.draw.circle(screen,red,mPos,rad)
    for ee in circList:
        #print(ee)
        if ee[1] <= 0:
            circList.remove(ee)
            ee[1] = 225
        pygame.draw.circle(screen,(ee[1],0,0),(ee[0][0],ee[0][1]),rad)
    pygame.display.flip()

pygame.display.quit()