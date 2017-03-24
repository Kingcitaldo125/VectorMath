# ---------------------------------------------------------------------------
#   This is a template that you can copy and rename to match your minigame  |
#                                                                           |
#   Follow the comments and you should be able to just throw the game in    |
#       with the rest with minimal difficulties...                          |
#                                                                           |
#                           ... Should.                                     |
# ---------------------------------------------------------------------------

# region ---------------- Imports --------------------
import minigames.minigame
from minigames.minigame import Minigame
from math3d import VectorN
import pygame
import time
import math
import random

# endregion


# region Classes or code specific to your minigame (like Player)
bulletRad = 5
enemyRad = 50
playerSpeed = 80 #Pixels per second
enemyList = []
class Player(object):
    def __init__(self,top,right,left,color):
        """Top Right and Left are the starting positions
        for the player """
        if( isinstance(top,list) == False):
            raise Exception("Must pass a list to the class")
        if(isinstance(right,list) == False):
            raise Exception("Must pass a list to the class")
        if(isinstance(left,list) == False):
            raise Exception("Must pass a list to the class")
        if(isinstance(color,tuple) == False):
            raise Exception("Must make sure color is a tuple")
        self.bulletList = []
        self.top = top
        self.right = right
        self.left = left
        self.color = color
        self.width = abs((self.right[0]-self.left[0])/2)
        self.offset = 50#should be the respective player width???
        self.playerScore = 0
        super().__init__()

    def movePlayer(self,param):
        """Player speed is global """
        if param == -1:
            self.top[0] -= playerSpeed
            self.left[0] -= playerSpeed
            self.right[0] -= playerSpeed

        elif param == 1:
            self.top[0] += playerSpeed
            self.left[0] += playerSpeed
            self.right[0] += playerSpeed

    def shootBullet(self):
        """This could also be the 'space bar' type event."""

    def playerBulletHit(self):
        """Enemy list should still be global var"""
        global numEnemies
        global enemiesKilled
        for e in enemyList[:]:
            for b in self.bulletList:
                if(( (b[0] - e[0])**2 + (b[1] - e[1])**2)**(0.5) <= (bulletRad+enemyRad)):
                    enemyList.remove(e)
                    self.bulletList.remove(b)
                    self.playerScore += 1
                    #Both globals
                    numEnemies-=1
                    enemiesKilled+=1

    def playerUpdate(self):
        """ """

    def playerUpdateCollide(self):
        """winx and zero are hardcoded """

        if self.left[0] <= 0:
            self.left[0] += self.offset
            self.right[0] += self.offset
            self.top[0] += self.offset

        if self.right[0] > self.winx:
            self.left[0] -= self.offset
            self.right[0] -= self.offset
            self.top[0] -= self.offset

    def bulletUpdate(self,delta,bspeed):
        """ """
        for e in self.bulletList:
            if e[1] <= 0:
                self.bulletList.remove(e)
            else:
                e[1] -= bspeed*delta

    def renderBullets(self,surf,tmscl):
        """ """
        for mie in self.bulletList:
            pygame.draw.circle(surf,tmscl,(int(mie[0]),int(mie[1])),bulletRad)

    def render(self,surf):
        """ """
        lineWidth = 5
        pygame.draw.polygon(surf,self.color,[self.top,self.left,self.right],lineWidth)

class Particles(object):
    def __init__(self):
        """ """
        self.particleList = []
        self.particleColor = (0,0,0)
        self.particlePos = [0,0]
        super().__init__()

    def createParticles(self):
        """ """
        colortemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        self.particlePos = [random.randrange(-10500,0),random.randrange(0,590)]
        self.particleColor = colortemp
        self.count = 0
        while self.count < 200:
            self.particleList.append({"Pos":self.particlePos,"Color":self.particleColor})
            self.count+=1

    def update(self,deltaT):
        """ """
        superspeed = 2000
        for kl in self.particleList:
            if(kl["Pos"][0] >= (5000)):
                kl["Pos"] = [random.randrange(-10500,0),random.randrange(0,590)]

            #print(kl["Pos"])
            kl["Pos"][0] += superspeed * deltaT

    def render(self,surf,cc):
        """ """
        partRad = 10
        for ptc in self.particleList:
            if powerupMode:
                pygame.draw.circle(surf,cc,(int(ptc["Pos"][0]),int(ptc["Pos"][1])),partRad)
            else:
                pygame.draw.circle(surf,ptc["Color"],(int(ptc["Pos"][0]),int(ptc["Pos"][1])),partRad)
class Enemy(object):
    def __init__(self):
        """Use the general enemy list made in main """
        #enemySpeed is global

    def update(self,dT):
        """ """
        global enemyList
        for m in enemyList:
            m[1] += enemySpeed*dT

    def generate(self,entot):
        """ """
        global enemyList
        num = 0
        while num < entot:
            enemyList.append([random.randrange(enemyRad,winx-enemyRad),random.randrange(-3500,-500),
            (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))])
            num+=1
        return enemyList

    def render(self,surf,col):
        """ """
        global enemyList
        rancol = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        for me in enemyList:
            pygame.draw.circle(surf,col,(int(me[0]),int(me[1])),enemyRad)

class Help(object):
    def __init__(self):
        """should do nothing """

    def display(self):
        """prints to console """
        stringone = "Use A & D to move"
        stringtwo = "Space to Shoot"
        stringthree = "Spam Space to shoot more"
        stringfour = "Stats at the top of the screen"
        print(stringone)
        print(stringtwo)
        print(stringthree)
        print(stringfour+"\n")

# endregion

class Game(Minigame):
    def __init__(self, pList):
        """ Put your initializing code here"""
        super().__init__(pList)
        self.name = "minigame_name"  # Change this out for the name of your minigame

        # region ----------- Put any code you need to run before the game starts in here ----------------

        #winy = 600

        #Colors
        self.yellow = (236,236,17)
        self.grey = (155,155,155)
        self.white = (255,255,255)
        self.blue = (0,0,255)
        self.red = (255,0,0)
        self.orange = (247,158,25)
        self.green = (0,255,0)
        self.cyan = (0,255,255)
        self.black = (0,0,0)

        self.selection = "medium"

        self.winx = 800
        self.winy = 600
        self.screen = pygame.display.set_mode((self.winx,self.winy))
        self.done = False
        self.win = False
        self.playerLength = 60 #Pixels

        self.playerwidth = 40

        #Generate Players
        #P1 - Red
        playeroneTop = [310,self.winy-self.playerLength]
        playeroneRight = [310+40,self.winy-10]
        playeroneLeft = [310-40,self.winy-10]
        pone = Player(playeroneTop,playeroneRight,playeroneLeft,self.red)
        #P2 - Blue
        playertwoTop = [250,self.winy-self.playerLength]
        playertwoRight = [290,self.winy-10]
        playertwoLeft = [210,self.winy-10]
        ptwo = Player(playertwoTop,playertwoRight,playertwoLeft,self.blue)
        #P3 - Green
        playerthreeTop = [500,self.winy-self.playerLength]
        playerthreeRight = [500+40,self.winy-10]
        playerthreeLeft = [500-40,self.winy-10]
        pthree = Player(playerthreeTop,playerthreeRight,playerthreeLeft,self.green)
        #P4 - Yellow?
        playerfourTop = [580,self.winy-self.playerLength]
        playerfourRight = [580+40,self.winy-10]
        playerfourLeft = [580-40,self.winy-10]
        pfour = Player(playerfourTop,playerfourRight,playerfourLeft,self.yellow)

        self.tempFont = pygame.font.Font(None,25)

        self.baseRanCol = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        self.cclr = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        self.clock = pygame.time.Clock()
        self.fillcolor = self.black

        #self.testList = []
        self.numEnemies = 0
        self.powerupchange = False

        self.change = 0.0

        if self.selection == "easy" or self.selection == "Easy":
            self.easy = True
            self.medium = False
            self.hard = False
        elif self.selection == "medium" or self.selection == "Medium":
            self.easy = False
            self.medium = True
            self.hard = False
        elif self.selection == "hard" or self.selection == "Hard":
            self.easy = False
            self.medium = False
            self.hard = True
        else:
            raise TypeError("Bad Input")


        #Speeds
        #bulletSpeed = 100 #Pixels per second

        if self.easy:
            self.enemySpeed = 80 #Pixels per second
        elif self.medium:
            self.enemySpeed = 100
        else:
            self.enemySpeed = 120

        #Ammo Setup
        self.num = 0

        #Calculate Difficulty
        if self.easy:
            self.total = 15
        elif self.medium:
            self.total = 25
        else:
            self.total = 55

        if self.easy:
            self.health = 100
        elif self.medium:
            self.health = 50
        else:
            self.health = 25

        self.numEnemies = self.total
        econtrol = Enemy()
        econtrol.generate(self.total)
        self.enemiesKilled = 0

        self.death = False
        self.powerupMode = False
        self.powerupTimer = 0
        self.spaceTimer = 0

        part = Particles()
        part.createParticles()
        #createParticles()

        self.wave = 1

        self.screen.fill(self.black)
        displayWave(self.screen)
        pygame.display.flip()
        time.sleep(2)
        self.getready = "Get Ready!"
        self.getS = tempFont.render(self.getready,True,self.white)
        self.screen.fill(black)
        self.screen.blit(self.getS,(int(self.winx/2),int(self.winy/2)))
        pygame.display.flip()
        time.sleep(2)

        #generateEnemies(total)
        self.waveTimer = 0

        # endregion

    def generalupdate(delta):
        #numEnemies
        part.update(delta)
        if self.powerupMode:
            self.bulletSpeed = 200
        else:
            self.bulletSpeed = 100
        econtrol.update(delta)
        pone.bulletUpdate(delta,self.bulletSpeed)
        ptwo.bulletUpdate(delta,self.bulletSpeed)
        pthree.bulletUpdate(delta,self.bulletSpeed)
        pfour.bulletUpdate(delta,self.bulletSpeed)

    def displayWave(surf):
        currWave = "Wave "+str(self.wave)
        waveS = tempFont.render(currWave,True,self.white)
        surf.blit(waveS,(int(self.winx/2),int(self.winy/2)))

    def fillScreen(color):
        self.screen.fill(color)

    def pickacolor():
        """ """
        xx = random.randrange(0,4)
        if xx == 0:
            return self.red
        elif xx == 1:
            return self.green
        elif xx == 2:
            return self.orange
        elif xx == 3:
            return self.cyan
        else:
            return self.blue

    def update(self, dt):
        """ Runs once every frame. Put all update code in here."""
        super().update(dt)
        # ------------- Code goes under here ----------
        self.updateColor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        generalupdate(dt)

        if self.powerupMode:
            if self.powerupTimer >= 8.0:
                #self.powerupTimer = 0
                self.powerupMode = False
                self.powerupchange = True
                self.powerupTimer = 0.0
            self.powerupTimer += 1*dT
            self.change+=1*dT
            #print(powerupTimer)

        if self.medium:
            if enemiesKilled >=10 and self.powerupchange == False:
                self.powerupMode = True
        elif easy:
            if self.enemiesKilled >= 5 and self.powerupchange == False:
                self.powerupMode = True
        elif hard:
            if self.enemiesKilled >= 40 and self.powerupchange == False:
                self.powerupMode = True

        if self.powerupMode == True:
            #pone.color
            pone.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            ptwo.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            pthree.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
            pfour.color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        else:
            pone.color = self.red
            ptwo.color = self.blue
            pthree.color = self.yellow
            pfour.color = self.green

        if(self.health <= 0):
            self.death = True

        if(self.numEnemies <=0):
            self.wave+=1
            self.screen.fill(self.black)
            displayWave(self.screen)#global funct
            pygame.display.flip()
            time.sleep(2)
            self.total+=10
            self.numEnemies=total
            del pone.bulletList[:]
            del ptwo.bulletList[:]
            del pthree.bulletList[:]
            del pfour.bulletList[:]
            econtrol.generate(self.total)
            self.enemySpeed+=10

        #Players wall collisions

        #Player one
        pone.playerUpdateCollide()

        #Player two
        ptwo.playerUpdateCollide()

        #Player three
        pthree.playerUpdateCollide()

        #Player four
        pfour.playerUpdateCollide()

        #Do the enemies reach the base???
        for mie in self.enemyList:
            if mie[1] >= self.winy-enemyRad:
                self.enemyList.remove(mie)
                self.numEnemies-=1
            if mie[1] + enemyRad >= self.winy:
                self.health-=10

        #Do Hit Detections
        pone.playerBulletHit()
        ptwo.playerBulletHit()
        pthree.playerBulletHit()
        pfour.playerBulletHit()


    def events(self, e):
        """ Any events your game handles will go in here. Use the format 'if e.type == x' where x is whatever you
        want to check"""
        super().events(e)
        # ------------- Code goes under here ----------
        eventlist = pygame.event.get()
        if self.powerupMode:
            if(pygame.key.get_pressed()[pygame.K_w]):
                if self.spaceTimer >= 0.2:
                    bulletColorTemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                    bulletSpawnPoint = [pone.top[0],pone.top[1],bulletColorTemp]
                    pone.bulletList.append(bulletSpawnPoint)
                    self.spaceTimer = 0

            if(pygame.key.get_pressed()[pygame.K_UP]):
                if self.spaceTimer >= 0.2:
                    bulletColorTemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                    bulletSpawnPoint = [ptwo.top[0],ptwo.top[1],bulletColorTemp]
                    ptwo.bulletList.append(bulletSpawnPoint)
                    self.spaceTimer = 0

            if(pygame.key.get_pressed()[pygame.K_i]):
                if self.spaceTimer >= 0.2:
                    bulletColorTemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                    bulletSpawnPoint = [pthree.top[0],pthree.top[1],bulletColorTemp]
                    pthree.bulletList.append(bulletSpawnPoint)
                    self.spaceTimer = 0

            if(pygame.key.get_pressed()[pygame.K_t]):
                if self.spaceTimer >= 0.2:
                    bulletColorTemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                    bulletSpawnPoint = [pfour.top[0],pfour.top[1],bulletColorTemp]
                    pfour.bulletList.append(bulletSpawnPoint)
                    self.spaceTimer = 0

            self.spaceTimer+=1*dT

        for ee in eventlist:
            if ee.type == pygame.KEYDOWN:
                #Player movement and shooting
                #Passing move parameters either 1 or -1 for right and left
                #respectively
                if ee.key == pygame.K_w:
                    if not powerupMode:
                        bulletColorTemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                        bulletSpawnPoint = [pone.top[0],pone.top[1],bulletColorTemp]
                        pone.bulletList.append(bulletSpawnPoint)

                if ee.key == pygame.K_a:#player one left
                    pone.movePlayer(-1)

                if ee.key == pygame.K_d: #player one right
                    pone.movePlayer(1)

                if ee.key == pygame.K_RIGHT:
                    ptwo.movePlayer(1)

                if ee.key == pygame.K_LEFT:
                    ptwo.movePlayer(-1)

                if ee.key == pygame.K_UP:
                    if not powerupMode:
                        bulletColorTemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                        bulletSpawnPoint = [ptwo.top[0],ptwo.top[1],bulletColorTemp]
                        ptwo.bulletList.append(bulletSpawnPoint)

                if ee.key == pygame.K_j:
                    pthree.movePlayer(-1)

                if ee.key == pygame.K_l:
                    pthree.movePlayer(1)

                if ee.key == pygame.K_i:
                    if not powerupMode:
                        bulletColorTemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                        bulletSpawnPoint = [pthree.top[0],pthree.top[1],bulletColorTemp]
                        pthree.bulletList.append(bulletSpawnPoint)

                if ee.key == pygame.K_t:
                    if not powerupMode:
                        bulletColorTemp = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
                        bulletSpawnPoint = [pfour.top[0],pfour.top[1],bulletColorTemp]
                        pfour.bulletList.append(bulletSpawnPoint)

                if ee.key == pygame.K_f:
                    pfour.movePlayer(-1)

                if ee.key == pygame.K_h:
                    pfour.movePlayer(1)

                if ee.key == pygame.K_ESCAPE:
                    self.done = True

    def render(self):
        """ Renders at the end of the game loop. All render code goes in here."""
        super().render()
        # ------------- Code goes under here ----------
        self.playeronemystr = "PLAYER ONE SCORE "
        self.playertwomystr = "PLAYER TWO SCORE "
        self.playerthreemystr = "PLAYER THREE SCORE "
        self.playerfourmystr = "PLAYER FOUR SCORE "
        #mystr = "asdasdasdd"

        self.enemyString = "Enemies Left: "+str(self.numEnemies)
        self.enemiesKilledString = "Enemies Killed: "+str(self.enemiesKilled)
        #ammostr = "AMMO"+" "+str(ammo)
        self.power = "POWERUP MODE!!!"
        self.scoreOneStr = self.playeronemystr+str(pone.playerScore)
        self.scoreTwoStr = self.playertwomystr+str(ptwo.playerScore)
        self.scoreThreeStr = self.playerthreemystr+str(pthree.playerScore)
        self.scoreFourStr = self.playerfourmystr+str(pfour.playerScore)
        self.scoreSone = tempFont.render(self.scoreOneStr,True,self.red)
        self.scoreStwo = tempFont.render(self.scoreTwoStr,True,self.blue)
        self.scoreSthree = tempFont.render(self.scoreThreeStr,True,self.green)
        self.scoreSfour = tempFont.render(self.scoreFourStr,True,self.yellow)
        self.healthS = tempFont.render("Base Health "+str(self.health),True,self.white)
        self.enemyS = tempFont.render(self.enemyString,True,self.white)
        self.enemyStwo = tempFont.render(self.enemiesKilledString,True,self.white)
        self.powerupS = tempFont.render(self.power,True,self.white)
        self.putS = tempFont.render(("Ends in: "+str((8-self.powerupTimer))),True,self.white)

        if self.powerupMode:
            if self.change >= 2.0:
                self.change = 0.0
                self.te = 0
                while self.te < 20:
                    self.te+=1
                    self.screen.fill(pickacolor())
        else:
            fillScreen(self.fillcolor)
            #Makes screen fill crazy fast and psychedelic like
            #fillScreen((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))

        #Draw players
        pone.render(self.screen)
        ptwo.render(self.screen)
        pthree.render(self.screen)
        pfour.render(self.screen)

        #Draw players' bullets
        pone.renderBullets(self.screen,self.cclr)
        ptwo.renderBullets(self.screen,self.cclr)
        pthree.renderBullets(self.screen,self.cclr)
        pfour.renderBullets(self.screen,self.cclr)

        if not self.powerupMode:
            #displayParticles(screen,updateColor)
            part.render(self.screen,self.updateColor)
        if self.powerupMode:
            #drawEnemies((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
            econtrol.render(self.screen,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
        else:
            #drawEnemies(baseRanCol)
            econtrol.render(self.screen,self.baseRanCol)

        self.screen.blit(self.scoreSone,(int(10),int(22)))
        self.screen.blit(self.scoreStwo,(int(10),int(42)))
        self.screen.blit(self.scoreSthree,(int(10),int(62)))
        self.screen.blit(self.scoreSfour,(int(10),int(82)))
        self.screen.blit(self.healthS,(int(self.winx/2),int(22)))
        self.screen.blit(self.enemyS,(int(self.winx-200),int(22)))
        self.screen.blit(self.enemyStwo,(int(self.winx/2),int(40)))
        if self.powerupMode:
            self.te = 0
            while self.te < 20:
                self.screen.blit(self.powerupS,(int(350),int(250)))
                self.screen.blit(self.putS,(int(350),int(300)))
                self.te+=1

        pygame.display.flip()

    def pmInit(val):
        """ This is used to set up the pregame menu for your minigame.
        Go through and change these strings."""
        if val == 1:
            # Replace this with a description of your game
            return "Defend your home planet from Asteroids!!!"
        elif val == 2:
            # Replace this return with the instructions for the game.
            hep = Help()
            return hep.display.stringone+hep.display.stringtwo\
            +hep.display.stringthree+hep.display.stringfour
        elif val == 3:
            # Replace this string with a screenshot of the minigame (it will auto-size it)
            return "spacess.png"
        elif val == 4:
            # Replace this string with whatever the directional inputs do
            return "Use the directional controls to move the player left-right"
        elif val == 5:
            # Replace this string with whatever the player's A button does
            return "A is not used"
        elif val == 6:
            # Replace this string with whatever the player's B button does
            return "B is not used"
