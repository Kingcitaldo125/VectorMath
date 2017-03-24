import pygame
import time

pygame.display.init()
pygame.font.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))

done = False
pressed = False
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
timer = 0.0
tempFont = pygame.font.Font(None,22)
#tempStr = "Current time: "+str(timer)
#tempS = tempFont.render(tempStr,True,white)

while not done:
    print(pressed)
    dT = clock.tick() / 1000.0
    if pressed == True:
        timer+=dT


    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if pressed == False:
                    pressed = True
                else:
                    pressed = False

            if e.key == pygame.K_ESCAPE:
                done = True

    screen.fill(black)
    tempStr = "Current time: "+str(timer)
    stopwatch = "stopwatch"
    tempS = tempFont.render(tempStr,True,white);
    tempS2 = tempFont.render(stopwatch,True,white)
    screen.blit(tempS,(int(10),int(10)))
    screen.blit(tempS2,(int(winx/2),int(winy/2)))
    # Used for debugging
    #print(timer)
    pygame.display.flip()

pygame.display.quit()