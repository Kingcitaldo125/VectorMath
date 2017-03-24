import pygame
import random
import math
import time

pygame.display.init()
pygame.font.init()

winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
red = (255,0,0)
white = (255,255,255)
brown = (204,102,0)
green = (0,255,0)
tw = 10
th = 10
clock = pygame.time.Clock()
tempFont = pygame.font.Font(None,22)
baseFont = pygame.font.Font(None,15)

enemyRad = 3

enemyList = []
towerList = []

money = 1500
rad_rad = 45
rad_posx = int(tw/2)
rad_posy = int(th/2)

basePosy = 0
basePosw = 100
basePosh = winy
basePosx = winx-basePosw

cur_enemy = 0
enemy_count = random.randrange(10,100)
speed = 50

done = False

chances = 10
cost = 155

ranr = random.randrange(0,255)
rang = random.randrange(0,255)
ranb = random.randrange(0,255)

ranr2 = random.randrange(0,255)
rang2 = random.randrange(0,255)
ranb2 = random.randrange(0,255)

ranr3 = random.randrange(0,255)
rang3 = random.randrange(0,255)
ranb3 = random.randrange(0,255)

ranr4 = random.randrange(0,255)
rang4 = random.randrange(0,255)
ranb4 = random.randrange(0,255)

while cur_enemy < enemy_count:
    enemyPosx = random.randint(-500,0)
    enemyPosy = random.randint(0,winy)
    enemyList.append([enemyPosx,enemyPosy])
    cur_enemy+=1

first_tower_posx = int(winx/2)
first_tower_posy = int(winy/2)
towerList.append([first_tower_posx,first_tower_posy])

baseHealth = basePosw

hit = False
hit_timer = 4
hit_timer_start = 0
hpLoss = float(10.0)

while not done:
    dt = clock.tick() / 1000.0
    #UPDATE
    if basePosx >= 800:
        #Lose Condition
        tempString = "YOU LOSE!!! ): "
        tempS = tempFont.render(tempString,True,white)
        screen.fill((0,0,0))
        screen.blit(tempS,(winx/2,winy/2))
        pygame.display.flip()
        time.sleep(3)
        done = True

    for tt in towerList:
        for e in enemyList:
            #Do some hit detection
            if math.sqrt( math.pow((e[0]- tt[0]),2) + math.pow((e[1]-tt[1]),2) ) < (enemyRad + rad_rad):
                enemyList.remove(e)
                cur_enemy-=1
                money+=45

    if cur_enemy <= 0:
        #Win condition
        tempString2 = "YOU WIN!!! :) "
        cur_enemy = 0
        tempS = tempFont.render(tempString2,True,white)
        screen.fill((0,0,0))
        screen.blit(tempS,(winx/2,winy/2))
        pygame.display.flip()
        time.sleep(4)
        done = True
    else:
        for eee in enemyList:
            #Are the enemies reaching the player's base??
            if eee[0] >= basePosx:
                #print(eee[0])
                enemyList.remove(eee)
                cur_enemy-=1
                basePosx+=basePosw/chances
                baseHealth-=basePosw/chances
                hit = True
        else:
            #ADVANCE ENEMY
            for ee in enemyList:
                ee[0] += speed*dt

    #INPUT
    events = pygame.event.get()
    mPos = pygame.mouse.get_pos()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
        if e.type == pygame.MOUSEBUTTONDOWN:
            if (money-cost)<=0:
                print("INSUFFICIENT FUNDS!")
                break;
            else:
                towerList.append(mPos)
                money-=cost

    #DRAW
    tempString3 = "$"+str(money)
    tempString4 = "Enemies Left: "+str(cur_enemy)
    baseString = "Base Health " + str(baseHealth)
    hitString = "HIT" + str(hpLoss)

    tempS3 = tempFont.render(tempString3,True,white)
    tempS4 = tempFont.render(tempString4,True,white)
    baseS = baseFont.render(baseString,True,white)
    hitS = tempFont.render(hitString,True,white)

    screen.fill((ranb2,rang2,ranr2))
    screen.blit(tempS3,(int(winx/2), int(winy-10)))
    screen.blit(tempS4,(int(winx/3), int(10)))
    screen.blit(baseS,(int((winx/2)+20 ), int(10)))
    print(hit_timer_start)
    if hit == True:
        while(hit_timer_start < hit_timer):
            if hit_timer_start > hit_timer:
                hit_timer_start = 0
            ranhitx = random.randrange(600,winx-20)
            ranhity = random.randrange(5,winy-20)
            screen.blit(hitS,(int(ranhitx),int(ranhity)))
            hit_timer_start+=1*dt
            #print(hit_timer_start)
        hit = False

#        print((ranhitxval,ranhity))

    #Draw Base
    pygame.draw.rect(screen,(ranb3,ranr3,rang3),(basePosx,basePosy,basePosw,basePosh))

    #Draw enemies
    for e in enemyList:
        pygame.draw.circle(screen,(ranb,rang,ranr),(int(e[0]),int(e[1])),enemyRad)

    #draw towers and their firing ranges
    for t in towerList:
        pygame.draw.rect(screen,(ranr4,rang4,ranb4),(t[0],t[1],tw,th))
        pygame.draw.circle(screen,white,(int(t[0]+rad_posx),int(t[1]+rad_posy)),rad_rad,1)
        #print(t)


    pygame.display.flip()
screen.fill((0,0,0))
pygame.display.quit()