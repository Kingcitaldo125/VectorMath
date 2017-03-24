import pygame
import random

pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
done = False
rad=1
white = (255,255,255)
snowballs = []
count=100
number=0

while number<count:
    ranx = random.randrange(0.0,float(winx))
    rany = random.randrange(-5000,-1000)
    snowballs.append([ranx,rany])
    number+=1
#print(snowballs)
while not done:
    #Update
    for i in snowballs:
        if i[1] > winy:
            i[1] = rany
        else:i[1]+=1
    print(snowballs)

    #input
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True

    #Draw
    screen.fill((0,0,0))
    for i in snowballs:
        pygame.draw.circle(screen,white,(i[0],i[1]),rad)

    pygame.display.flip()
pygame.display.quit()