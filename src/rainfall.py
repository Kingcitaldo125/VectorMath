import pygame
import random

pygame.display.init()

winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
done = False
cur_drops = 0
num_drops = 50
drops = []
white = (255,255,255)
clock = pygame.time.Clock()
speed = 1

while cur_drops < num_drops:
    ransx1 = random.randrange(0,winx-1)
    ransx2 = ransx1
    ransy1 = random.randrange(-55,-20)
    ransy2 = random.randrange(-20,0)

    start_pos = (ransx1,ransy1)
    end_pos = (ransx2,ransy2)
    drops.append([start_pos,end_pos])
    cur_drops+=1

myLineStart = (250,20)
myLineEnd = (250,45)

while not done:
    dT = clock.tick() / 1000.0
    for eee in drops:
        if eee[1][1] >= winy:
            drops.remove(eee)
        #eee[0][1]+=speed
        #eee[1][1]+=speed
    myLineStart[1]+=10
    #myLineEnd[1]+10
    print(myLineStart)
    #print(myLineEnd)

    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True

    for i in drops:
        pygame.draw.line(screen,white,i[0],i[1])
    pygame.draw.line(screen,white,myLineStart,myLineEnd)
    pygame.display.flip()


pygame.display.quit()