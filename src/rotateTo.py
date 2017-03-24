import pygame
import math

def angleToRotateBy(one, two):
    dot = one.dot(two)
    magProduct = one.length() * two.length()

    if magProduct != 0:
        division = dot / magProduct
        thetaRads = math.acos(division)
        thetaDegs = math.degrees(thetaRads)
        return thetaDegs*0.5 #print(thetaDegs)
    return 0.005
    
pygame.display.init()

screen = pygame.display.set_mode((800, 600))

done = False

rectPos = pygame.math.Vector2(400, 300)

clock = pygame.time.Clock()
while not done:
    dT = clock.tick() / 1000.0
    mPosGame = pygame.mouse.get_pos()
    mPosVec = pygame.math.Vector2(mPosGame[0], mPosGame[1])

    #Rotate rect object
    theta = rectPos.angle_to(mPosVec) #theta = angleToRotateBy(rectPos, mPosVec)

    #Rotate
    rectPos.x = 10*math.cos(theta) - 10*math.sin(theta)
    rectPos.y = 10*math.sin(theta) + 10*math.cos(theta)
    
    #Then translate
    rectPos.x += 400
    rectPos.y += 300
    
    events = pygame.event.get()

    for e in events:
        if e.type== pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))
    
    pygame.draw.line(screen, (255, 255, 255), (rectPos.x+(35/2), rectPos.y+(35/2)), (mPosVec.x, mPosVec.y))
    pygame.draw.rect(screen, (25, 100, 50), (int(rectPos.x), int(rectPos.y), 35, 35))
    pygame.display.flip()
    
pygame.display.quit()
