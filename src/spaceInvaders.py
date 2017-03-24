import pygame
import time
import math
import random

numEnemies = 0

def player():
    startx = winx/2
    starty = winy-playerLength

def drawPlayer(playerTop,playerRight,playerLeft):
    lineWidth = 5
    pygame.draw.polygon(screen,grey,[playertop,playerLeft,playerRight],lineWidth)

def drawBullets():
    for ie in bulletList:
        pygame.draw.circle(screen,white,(int(ie[0]),int(ie[1])),bulletRad)

def drawEnemies():
    rancol = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    for me in enemyList:
        pygame.draw.circle(screen,rancol,(int(me[0]),int(me[1])),enemyRad)

def fillScreen(color):
    screen.fill(color)

def generateEnemies(entot):
    """ """
    global num
    while num < entot:
        enemyList.append([random.randrange(0,winx),random.randrange(-4500,-10)])
        num+=1


def getInput():
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                bulletList.append()
            if e.key == pygame.K_a:
                start
            if e.key == pygame.K_ESCAPE:
                done = True

def update():
    global numEnemies
    for m in enemyList:
        if m[1] >= winy-enemyRad:
            enemyList.remove(m)
            numEnemies-=1
        else:
            m[1] += enemySpeed*dT

    for e in bulletList:
        if e[1] <= 0:
            bulletList.remove(e)
        else:
            e[1]-=bulletSpeed*dT

pygame.display.init()
pygame.font.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
done = False
playerLength = 60 #Pixels

playerwidth = 40
playertop = [winx/2,winy-playerLength]
playerRight = [360,winy-10]
playerLeft = [440,winy-10]

tempFont = pygame.font.Font(None,25)

grey = (155,155,155)
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()

bulletList = []
testList = []
bulletRad = 5
enemyList = []
#numEnemies = 0
enemyRad = 50

#Difficulty Selection
selection = input("Enter the Difficulty: (easy medium hard)")
str(selection)

if selection == "easy" or selection == "Easy":
    easy = True
    medium = False
    hard = False
elif selection == "medium" or selection == "Medium":
    easy = False
    medium = True
    hard = False
elif selection == "hard" or selection == "Hard":
    easy = False
    medium = False
    hard = True
else:
    raise TypeError("Bad Input")


#Speeds
bulletSpeed = 100 #Pixels per second

if easy:
    enemySpeed = 80 #Pixels per second
elif medium:
    enemySpeed = 150
else:
    enemySpeed = 200

playerSpeed = 100 #Pixels per second

#Ammo Setup
num = 0

if easy:
    ammo = 50
elif medium:
    ammo = 25
else:
    ammo = 10

#Calculate Difficulty
if easy:
    total = 15
elif medium:
    total = 25
else:
    total=55

numEnemies=total
print(numEnemies)
score = 0
health = 100

death = False
powerupMode = False

generateEnemies(total)

while not done:
    #Update
    dT = clock.tick() / 1000.0
    update()
    if(health <= 0):
        death = True
    if playerRight[0] < 0:
        playerLeft[0] += 50
        playerRight[0] += 50
        playertop[0] += 50

    if playerLeft[0] > winx:
        playerLeft[0] -= 50
        playerRight[0] -= 50
        playertop[0] -= 50

    #Do Hit Detections
    for e in enemyList:
        if e[1] + enemyRad >= winy:
            health-=10

        for bb in bulletList:
            if bb != e and e != bb:
                if(math.sqrt( (bb[0] - e[0])**2 + (bb[1] - e[1])**2 ) <= (bulletRad+enemyRad)):
                    enemyList.remove(e)
                    bulletList.remove(bb)
                    score+=1
                    ammo+=1


    #input
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            #Move the player
            if e.key == pygame.K_SPACE:
                if ammo <=0:
                    break;
                bulletSpawnPoint = [playertop[0],playertop[1]]
                testList.append(10)
                bulletList.append(bulletSpawnPoint)
                ammo-=1

            if e.key == pygame.K_a:
                playertop[0]-=playerSpeed
                playerLeft[0]-=playerSpeed
                playerRight[0]-=playerSpeed

            if e.key == pygame.K_d:
                playertop[0]+=playerSpeed
                playerLeft[0]+=playerSpeed
                playerRight[0]+=playerSpeed

            if e.key == pygame.K_ESCAPE:
                done = True

    #Draw
    mystr = "SCORE"
    enemyString = "Enemies Left "+str(total)
    ammostr = "AMMO"+" "+str(ammo)
    scoreStr = str(score)
    nameS = tempFont.render(mystr,True,white)
    scoreS = tempFont.render(scoreStr,True,white)
    ammoS = tempFont.render(ammostr,True,white)
    healthS = tempFont.render("Health "+str(health),True,white)
    fillScreen(black)
    drawPlayer(playertop,playerRight,playerLeft)
    drawBullets()
    drawEnemies()
    screen.blit(scoreS,(int(72),int(22)))
    screen.blit(nameS,(int(4),int(22)))
    screen.blit(healthS,(int(winx/2),int(42)))
    screen.blit(ammoS,(int(5),int(42)))
    pygame.display.flip()
    if(death == True):
        screen.fill(black)
        looseS = tempFont.render("You Loose..",True,white)
        screen.blit(looseS,(int(winx/2),int(winy/2)))
        pygame.display.flip()
        time.sleep(2.5)
        done = True
pygame.display.quit()
