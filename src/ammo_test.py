def reload(c,m,r):
    """ """
    reloader = m-c
    r-=reloader
    return reloader

import math
import pygame
import random

pygame.display.init()
pygame.mixer.init()
#reload_sound = pygame.mixer.Sound(Gun_Cocking_Slow-Mike_Koenig-1019236976)
#shooter_sound = pygame.mixer.Sound(barreta_m9-Dion_Stapper-1010051237)
winx = 400
winy = 400
black = (0,0,0)
red = (255,0,0)
rad = 5
ammo_max = 6
ammo_cur = 6
ammo_res = 26
screen = pygame.display.set_mode((winx,winy))

bullet_list = []

done = False
while not done:
    #update
    print(ammo_cur,ammo_res)
    if ammo_cur < 0:
        ammo_cur = 0;
    if ammo_res <= 0:
        ammo_res=0
        if ammo_cur <=0:
            done == True
            #raise TypeError("OUT OF AMMO!!!!!")

    #if ammo_cur<1:
    #    reloader=ammo_max-ammo_cur
    #    while(ammo_cur<ammo_max):
    #        #reloader = ammo_max-ammo_cur
    #        ammo_cur+=reloader
    #        ammo_res-=reloader

    #input
    events = pygame.event.get()
    mPos = pygame.mouse.get_pos()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done=True
            elif e.key == pygame.K_r:
                #Break
                if(ammo_res <= 0):
                    print("NO AMMO")
                    break;
                elif (ammo_cur > ammo_res):
                    #reload a certain way
                    print(str(ammo_res)+"Ammo reserves")
                    reloader = abs(ammo_cur - ammo_res)
                    print(str(ammo_res)+"Reserve ammo")
                    print(str(ammo_cur)+"Current ammo")
                    ammo_res -= reloader
                    ammo_cur += reloader
                else:
                    #reload
                    reloader=ammo_max-ammo_cur
                    while(ammo_cur<ammo_max):
                    #reloader = ammo_max-ammo_cur
                        ammo_cur+=reloader
                        ammo_res-=reloader

        if e.type == pygame.MOUSEBUTTONDOWN:
            if ammo_cur == 0:
                break
            else:
                bullet_list.append(mPos)
                ammo_cur-=1

    #draw
    screen.fill(black)
    for i in bullet_list:
        #print(i)
        pygame.draw.circle(screen,red,(i[0],i[1]),rad)
    pygame.display.flip()
pygame.display.quit()