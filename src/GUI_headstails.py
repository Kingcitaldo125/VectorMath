import pygame
import random
import time

pygame.display.init()
pygame.font.init()
winx = 400
winy = 400
white = (255,255,255)
screen = pygame.display.set_mode((winx,winy))
tempFont = pygame.font.Font(None,22);

random1 = random.randint(0,1)
if random1 == 0:
    result = "Heads"
else:
    result = "Tails"
tempStr = str(result)
tempS = tempFont.render(tempStr,True,white)




screen.blit(tempS,(winx/2,winy/2))
pygame.display.flip()
#print("result = "+result)
time.sleep(2)
pygame.font.quit()
pygame.display.quit()