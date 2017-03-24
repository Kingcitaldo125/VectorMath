import pygame
import random
import time

pygame.display.init()
screen = pygame.display.set_mode((800,600))
color = (255,255,255)

pygame.draw.circle(screen, color,  (random.randint(0,799),random.randint(0,599)),40,1)




pygame.display.flip()
time.sleep(2)
pygame.display.quit()