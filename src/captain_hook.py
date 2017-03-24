import pygame
import math3d


pygame.display.init()
pygame.font.init()
f = pygame.font.SysFont("Courier New", 16)
screen = pygame.display.set_mode((800,600))
done = False


Pts = [[math3d.VectorN((100,400)), "C"], \
     [math3d.VectorN((750,200)), "S"], \
     [math3d.VectorN((550,50)), "M"], \
     [math3d.VectorN((780,400)), "L"]]


while not done:
    # Update
    C = Pts[0][0]
    S = Pts[1][0]
    M = Pts[2][0]
    L = Pts[3][0]

    # Quiz computations
    Qhat = (S - C).normalized_copy()
    A = C + 550 * Qhat
    T = A - M
    That = T.normalized_copy()
    B = A + 380 * That
    Uhat = (L - B).normalized_copy()
    X = B + 100 * Uhat


    # Input
    eList = pygame.event.get()
    for e in eList:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = True
        if e.type == pygame.MOUSEBUTTONDOWN:
            # Select vertex
            pass


    # Draw
    screen.fill((0,0,0))
    for p in Pts:
        x, y = p[0].toIntTuple()
        pygame.draw.circle(screen, (255,255,255), (x,y), 6)
        screen.blit(f.render(p[1], False, (255,255,255)), (x, y-22))

    pygame.draw.circle(screen, (255,0,0), T.toIntTuple(), 8)

    pygame.draw.line(screen, (128,128,128), C.toIntTuple(), A.toIntTuple())
    pygame.draw.line(screen, (128,128,128), A.toIntTuple(), B.toIntTuple())
    pygame.draw.line(screen, (128,128,128), B.toIntTuple(), X.toIntTuple())



    pygame.display.flip()

pygame.display.quit()