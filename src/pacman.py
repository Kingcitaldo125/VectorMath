import pygame
import random
import time

pygame.display.init()

winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))

yellow = (255,255,0)
black = (0,0,0)
x=400
y=300
pacman_pos = (x,y)
pacman_rad = 50
degrees=50

pygame.draw.circle(screen,yellow,pacman_pos,pacman_rad)

lines_drawn = 0
while lines_drawn < degrees:
    pygame.draw.line(screen,black,pacman_pos,(x+pacman_rad,y-25))
    y+=1
    lines_drawn+=1



print("PacMan's radius = "+str(pacman_rad))
print("PacMan's mouth angle = "+str(degrees)+" degrees")
print("PacMan's pos = "+str(pacman_pos))
pygame.display.flip()
time.sleep(3)
pygame.display.quit()