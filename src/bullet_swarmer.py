import pygame
import random

pygame.display.init()
win_width = 800
win_height = win_width - 200
leftx = 10
topy = 10
screen = pygame.display.set_mode((win_width,win_height))
done = False
BulletList = []
ranr = random.randrange(0,255)
rang = random.randrange(0,255)
ranb = random.randrange(0,255)
ran2r = random.randrange(0,255)
ran2g = random.randrange(0,255)
ran2b = random.randrange(0,255)

bulletcolor = (ranr,rang,ranb)
rad = 5
bulletdraw = True

while not done:
    #UPDATE#
    #print(BulletList)
    for i in BulletList:
        if i[0] < mx:
            i[0]+=1
        elif i[1] < my:
            i[1]+=1
        elif i[0] > mx:
            i[0]-=1
        elif i[1] > my:
            i[1]-=1
        elif i[0] == mx:
            BulletList.remove(i)
        elif i[1] == my:
            BulletList.remove(i)

    #INPUT#
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
    keypressed = pygame.key.get_pressed()
    mousepressed = pygame.mouse.get_pressed()
    mx,my = pygame.mouse.get_pos()
    #mx = win_width/2
    #my = win_height/2
    if mousepressed == (1,0,0):
        bulletspawnx = random.randint(1,win_width)
        bulletspawny = random.randint(1,win_height)
        BulletList.append([bulletspawnx,bulletspawny])
        #pygame.draw.circle(screen, bulletcolor, (bulletspawnx, bulletspawny),rad)

    #DRAW#
    screen.fill((ran2r,ran2g,ran2b))
    if bulletdraw == True:
        #pygame.draw.circle(screen, bulletcolor, (bulletspawnx, bulletspawny),rad)
        #bulletdraw = False
        for i in BulletList:
            pygame.draw.circle(screen, bulletcolor, (i[0],i[1]),rad)
        #bulletdraw = False
    #print(mousepressed)
    pygame.display.flip()

pygame.display.quit()
