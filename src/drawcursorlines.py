def drawCursor():
    pygame.draw.line(screen,red,(halfx-20,halfy),(halfx-10,halfy),width)
    pygame.draw.line(screen,red,(halfx,halfy-20),(halfx,halfy-10),width)
    pygame.draw.line(screen,red,(halfx+20,halfy),(halfx+10,halfy),width)
    pygame.draw.line(screen,red,(halfx,halfy+20),(halfx,halfy+10),width)



import pygame
import time

winx = 800
winy = 600
pygame.display.init()
screen = pygame.display.set_mode((winx,winy))
red = (255,0,0)
halfx = winx/2
halfy = winy/2
width = 5

drawCursor()

pygame.display.flip()
time.sleep(3)
pygame.display.quit()