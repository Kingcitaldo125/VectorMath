import pygame
import time
import sys
import random
import math

pygame.display.init()
pygame.font.init()
winx = 800
winy = 600
done = False
screen = pygame.display.set_mode((winx,winy))
clock = pygame.time.Clock()

red = (255,0,0)
white = (255,255,255)
teal = (0,255,255)
blue = (0,0,255)
speed = 50

player1score = 0
player2score = 0

player1rad = 30
player2rad = player1rad
player1col = red
player2col = blue

p1x = 100
p1y = 250
p2x = winx-150
p2y = 250

player1pos = (p1x,p1y)
player2pos = (p2x,p2y)

bulletRad = 5

masterList1 = []
masterList2 = []

def draw():
    """ """
    grey = (160,160,160)
    screen.fill(grey)
    #Draw players
    pygame.draw.circle(screen,red,(int(p1x),int(p1y)),player1rad)
    pygame.draw.circle(screen,blue,(int(p2x),int(p2y)),player2rad)

    for ee in masterList1:
        randomr = random.randrange(0,255)
        randomg = random.randrange(0,255)
        randomb = random.randrange(0,255)
        randCol = (randomr,randomg,randomb)
        pygame.draw.circle(screen,randCol,(ee[0],ee[1]),bulletRad)

    for eie in masterList2:
        randomr = random.randrange(0,255)
        randomg = random.randrange(0,255)
        randomb = random.randrange(0,255)
        randCol = (randomr,randomg,randomb)
        pygame.draw.circle(screen,randCol,(eie[0],eie[1]),bulletRad)

    tempFont = pygame.font.Font(None,22)
    tempStr = "Player 1 score "+str(player1score)
    tempStr2 = "Player 2 score "+str(player2score)
    tempSplayer1 = tempFont.render(tempStr,True,red)
    tempSplayer2 = tempFont.render(tempStr2,True,blue)
    screen.blit(tempSplayer1,(int(30),int(10)))
    screen.blit(tempSplayer2,(int(winx-140),int(10)))
    pygame.display.flip()

def inputv():
    """ """
    global p1x
    global p1y
    global p2x
    global p2y

    kstate = pygame.key.get_pressed()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            #Move player one:
            if event.key == pygame.K_w:
                p1y-=speed
            if event.key == pygame.K_s:
                p1y+=speed
            #Move player two
            if event.key == pygame.K_UP:
                p2y-=speed
            if event.key == pygame.K_DOWN:
                p2y+=speed

            #Player 1 input
            if event.key == pygame.K_SPACE:
                onenewcircx = p1x
                onenewcircy = p1y
                masterList1.append([onenewcircx,onenewcircy])

            #Player 2 input
            if event.key == pygame.K_RSHIFT:
                newcircx = p2x
                newcircy = p2y
                masterList2.append([newcircx,newcircy])

            if event.key == pygame.K_ESCAPE:
                pygame.display.quit(); sys.exit()

def hitDetect():
    """ """
    global player1score
    global player2score

    for ie in masterList1:
        if ie[0] >= winx:
            player1score+=1
            masterList1.remove(ie)
    for eee in masterList2:
        if eee[0] <= 0:
            player2score+=1;
            masterList2.remove(eee)

    for ll in masterList2:
        sub0 = (abs(ll[0] - p1x))
        sub00 = (abs(ll[1] - p1y))
        radsum0 = bulletRad + player1rad
        if math.sqrt( (sub0**2) + (sub00**2)) <= radsum0:
            #Hit = True
            masterList2.remove(ll)

    for l in masterList1:
        sub1 = (abs(l[0] - p2x))
        sub2 = (abs(l[1] - p2y))
        radsum = bulletRad + player2rad
        if math.sqrt( (sub1**2) + (sub2**2) ) <= radsum:
            #Hit = True
            masterList1.remove(l)

def main():
    """ """
    global p1y
    global p2y
    #global total
    global player1score
    global player2score

    while True:
        #player 1 bounds
        if (p1y - player1rad) <= 0:
            p1y = player1rad
        if (p1y + player1rad) >= winy:
            p1y = winy - player1rad

        #player 2 bounds
        if (p2y - player2rad) <= 0:
            p2y = player2rad
        if (p2y + player2rad) >= winy:
            p2y = winy - player2rad

        hitDetect()
        inputv()
        dT = clock.tick() / 1000.0
        for w in masterList2:
            if w[0] <= 0:
                masterList2.remove(w)
            w[0] -= 1

        for ine in masterList1:
            if ine[0] >= winx:
                masterList1.remove(ine)
            ine[0] += 1

        draw()
        print(masterList1)
    pygame.display.quit()

if __name__ == '__main__':
    main()
