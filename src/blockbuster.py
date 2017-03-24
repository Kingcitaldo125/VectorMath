# blockbuster

#Using a one based system for player position

import pygame
import random
import time

winx = 800
winy = 600
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((winx,winy))
masterBulletList = []
clock = pygame.time.Clock()

class Player(object):
    def __init__(self,x,y):
        """ """
        self.x = x
        self.y = y
        self.width = 20
        self.height = 50
        self.color = (155,155,155)
        self.bulletStartx = (self.x + (self.width/2))
        self.bulletStarty = self.y

    def checkPlayerCollision(self):
        """ """
        if(self.x + self.width > winx):
            self.x = winx-self.width

        if(self.x <= 0):
            self.x = 1


    def returnAttribute(self):
        """ """
        return (self.x,self.y)

    def draw(self,surface):
        """ """
        pygame.draw.rect(surface,self.color,(self.x,self.y,self.width,self.height),0)

    def fire(self):
        """ """
        masterBulletList.append([plr.x,self.bulletStarty])
        print("Appended New Bullet to master list")

class Block(object):
    def __init__(self,x,y):
        """ """
        self.width = 100
        self.height = 50
        self.x = x
        self.y = y
        self.velocity = 100#pix per second
        self.foreward = True
        self.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    def move(self,dT):
        """ """
        #print(self.x)
        if self.foreward:
            for nie in blockList:
                nie[0]+=self.velocity*dT
            #self.x+=self.velocity * dT
        else:
            for nie in blockList:
                nie[0]-=self.velocity*dT
            #self.x-=self.velocity * dT

    def checkCollision(self):
        """ """
        for some in blockList:
            if (some[0] + self.width) > winx:
                self.foreward = False
                some[0] = winx-self.width
            if some[0] <= 0:
                self.foreward = True
                some[0] = 1

    def getPos(self):
        """ """
        tempList = []
        tempAttribute = [self.x,self.y]
        tempList.append(tempAttribute)
        return tempAttribute


tempfont = pygame.font.Font(None,25)
done = False
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
tempranx = random.randrange(1,winx)
temprany = 20
blk = Block(tempranx,temprany)
blockList = []
blockList.append([blk.x,blk.y,blk.color])

startx = winx/2
starty = winy-20
plr = Player(startx,starty)

playerxVel = 80
playerxVel2 = 80
bulletvel = 250
bulletRad = 15

score = 0

while not done:
    globalTime = clock.tick() / 1000.0
    #print(globalTime)
    events = pygame.event.get()
    mPos = pygame.mouse.get_pos()

    blk.move(globalTime)
    blk.checkCollision()
    plr.checkPlayerCollision()

    #print(blockList)
    for blt in masterBulletList:
        blt[1]-=bulletvel*globalTime
        if (blt[1]-bulletRad) <= 0:
            masterBulletList.remove(blt)
        for block in blockList:
            if (blt[0]) > block[0] and (blt[0]) <= (block[0]+blk.width):
                if (blt[1] - bulletRad) > block[1] and (blt[1] - bulletRad) <= (block[1]+blk.height):
                    masterBulletList.remove(blt)
                    del masterBulletList[:]
                    blockList.remove(block)
                    tempx = random.randrange(1,winx)
                    nublock = Block(tempx,20)
                    blockList.append([nublock.x,nublock.y,nublock.color])
                    score += 1

    #inputs
    for e in events:
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                plr.x -= playerxVel2
            if e.key == pygame.K_d:
                plr.x += playerxVel
            if e.key == pygame.K_ESCAPE:
                done = True
            if e.key == pygame.K_SPACE:
                plr.fire()
                print("Firing")

    screen.fill(black)

    string = "Score: " + str(score)
    blockbuster = "Paul's Block Buster!"
    blockS = tempfont.render(blockbuster,True,white)
    scoreS = tempfont.render(string,True,white)

    plr.draw(screen)

    for blt in masterBulletList:
        pygame.draw.circle(screen,(55,55,55),(int(blt[0]),int(blt[1])),bulletRad,0)
    #Draw the block
    for tbk in blockList:
        pygame.draw.rect(screen,tbk[2],(tbk[0],tbk[1],blk.width,blk.height))
    screen.blit(scoreS,(10,10))
    screen.blit(blockS,((winx/2)-50,(winy/2)))
    pygame.display.flip()
pygame.font.quit()
pygame.display.quit()