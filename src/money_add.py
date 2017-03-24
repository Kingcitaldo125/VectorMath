import pygame
import time

pygame.display.init()

winx = 800
winy = 600
screen = pygame.display.set_mode((winx,winy))
done = False
clock = pygame.time.Clock()
timer = 0.1
money = 0
total = 1500

while not done:
    events = pygame.event.get()
    dT = clock.tick() / 1000.0

    while money < total:
        money+=timer*dT
    for e in events:
        if e.type == pygame.MOUSEBUTTONDOWN:
            money+=timer*dT
        if e.type == pygame.KEYDOWN:
            done = True



    print(money)
    pygame.display.flip()

pygame.display.quit()