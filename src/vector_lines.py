import math3d
import math
import pygame

pygame.display.init()
winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
white = (255,255,255)
red = (255,0,0)


done = False

P = math3d.VectorN((400,300)) #Player pos
E = math3d.VectorN((100,100)) #Enemy Pos

while not done:
    B = P - E
    Ehat = E.normalized_copy()
    Phat = P.normalized_copy()
    Bhat = B.normalized_copy()

    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True


    pygame.draw.line(screen,white,E,P)
    pygame.draw.line(screen,red,E,Phat)
    pygame.display.flip()
    print(Bhat)

pygame.display.quit()