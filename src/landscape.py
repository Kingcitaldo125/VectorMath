import pygame
import time

pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))

#Grass#
grass_bot_lef = [10,winy-10]
grass_bot_right = [10,winy-10]
grass_top = [50,winy-20]
green = (0,255,0)

#grass_bot_lef.append(0,winy)
#grass_bot_right.append([5,winy])
#grass_top.append([50,winy-20])
num_triangle = 0
#print(grass_bot_lef)
while num_triangle < 1000:
    pygame.draw.polygon(screen,green,[grass_bot_lef, grass_top ,grass_bot_right],5)
    grass_bot_lef[0]+=1
    grass_top[0]+=1
    grass_bot_right[0]+=1
    num_triangle+=1


pygame.display.flip()
time.sleep(2)
pygame.display.quit()