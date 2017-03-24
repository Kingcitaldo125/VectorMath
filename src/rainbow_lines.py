import pygame
import time
import random

winx = 800
winy = 600
pygame.display.init()
screen = pygame.display.set_mode((winx,winy))

pt_list = []
cur_pt = 0
total_pt = 7

#ran_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
#pt1 = (random.randint(0,800),random.randint(0,600))

while cur_pt < total_pt:
    #ran_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    ran_start = (random.randint(0,winx),random.randint(0,winy))
    ran_end = (random.randint(0,winx),random.randint(0,winy))
    pt_list.append((ran_start,ran_end))

    #for i in pt_list:
     #   print(i)
     #   print(i[0])
     #   print(i[1])
    cur_pt+=1

#Draw Lines

#@@@ COLORS @@@#
color_list = []
white = (255,255,255)

blue = (0,0,255) #0
red = (255,0,0) #1
yellow = (255,255,0) #2
orange = (250,106,22) #3
cyan = (51,255,255) #4
green = (0,204,0) #5
violet = (153,0,153) #6

color_list.append(blue)
color_list.append(red)
color_list.append(yellow)
color_list.append(orange)
color_list.append(cyan)
color_list.append(green)
color_list.append(violet)

ran_color1 = color_list[random.randrange(0,6)]
ran_color2 = color_list[random.randrange(0,6)]
ran_color3 = color_list[random.randrange(0,6)]
ran_color4 = color_list[random.randrange(0,6)]
ran_color5 = color_list[random.randrange(0,6)]
ran_color6 = color_list[random.randrange(0,6)]
ran_color7 = color_list[random.randrange(0,6)]

screen.fill((0,0,0))

pygame.draw.line(screen,ran_color1,(pt_list[0][0]),(pt_list[0][1]))

pygame.draw.line(screen,ran_color2,(pt_list[0][1]),(pt_list[1][0]))

pygame.draw.line(screen,ran_color3,(pt_list[1][0]),(pt_list[1][1]))

pygame.draw.line(screen,ran_color4,(pt_list[1][1]),(pt_list[2][0]))

pygame.draw.line(screen,ran_color5,(pt_list[2][0]),(pt_list[2][1]))

pygame.draw.line(screen,ran_color6,(pt_list[2][1]),(pt_list[3][0]))

pygame.draw.line(screen,ran_color7,(pt_list[3][0]),(pt_list[3][1]))

pygame.draw.line(screen,white,(pt_list[3][1]),(pt_list[0][0]))

print(color_list)

pygame.display.flip()
time.sleep(3)
pygame.display.quit()