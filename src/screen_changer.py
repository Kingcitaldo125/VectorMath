import pygame
import random

pygame.display.init()
pygame.font.init()
tr = 255
tg = 255
tb = 255
tempSCOL = (tr,tg,tb)
tempFont = pygame.font.Font(None,22)
tempStr = "Press 'a' to change Red 's' to change Green and 'd' to change Blue and Space to default"

winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
objs = []

done = False
r = 0
g = 0
b = 0

while done != True:
    #Update
    tempSCOL = (tr,tg,tb)
    screen_col = (r,g,b)
    print(screen_col)

    #input
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
            if e.key == pygame.K_a:
                r=random.randrange(0,255)
            if e.key == pygame.K_d:
                b=random.randrange(0,255)
            if e.key == pygame.K_s:
                g=random.randrange(0,255)
            if e.key == pygame.K_RETURN:
                #Make the tempS color black!
                tr = 0
                tg = 0
                tb = 0
                r=255
                g=255
                b=255
            if e.key == pygame.K_SPACE:
                tr = 255
                tg = 255
                tb = 255
                r=0
                g=0
                b=0

    #Draw
    tempS = tempFont.render(tempStr,True,tempSCOL)
    screen.fill(screen_col)
    screen.blit(tempS,(0,0))
    pygame.display.flip()

pygame.font.quit()
pygame.display.quit()