import pygame
import math
import math3d
import random


pygame.display.init()
winx=800;winy=600
screen = pygame.display.set_mode((winx,winy))
clock = pygame.time.Clock()
done = False
hwinx= int(winx/2)
hwiny= int(winy/2)

L = math3d.VectorN((hwinx,hwiny))#Link's pos
B = math3d.VectorN((100,550))#beamos pos
n = 50
alpha = 3*math.pi/2     # In radians
fill = 0
speed=32

while not done:
    # UPDATE
    dT = clock.tick() / 1000.0
    alpha += (math.pi / speed) * dT

    # Step1 in symbolic proof
    shat = math3d.VectorN((math.cos(alpha), math.sin(alpha)))
    E = B + 2000 * shat

    # Step2 in symbolic proof
    D = L - B

    # Step3 in symbolic proof
    Dpara = shat * math3d.dot(D, shat)
    Dperp = D - Dpara

    # Step4 in symbolic proof
    if Dperp.magnitude() <= n and math3d.dot(D, shat) > 0:
        fill = 1
    else:
        fill = 0

    # INPUT
    pygame.event.get()
    kPress = pygame.key.get_pressed()
    mPress = pygame.mouse.get_pressed()
    mPos = pygame.mouse.get_pos()
    if kPress[pygame.K_ESCAPE]:
        done = True
    if mPress[0]:
        L = math3d.VectorN(mPos)
    if mPress[2]:
        B = math3d.VectorN((hwinx,hwiny))

    # DRAW
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (0,255,0), L.toIntTuple(), n, fill)
    pygame.draw.circle(screen, (255,0,0), B.toIntTuple(), 5)
    pygame.draw.line(screen, (255,255,255), B, E)

    pygame.display.flip()

pygame.display.quit()
