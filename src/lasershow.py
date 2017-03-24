import pygame
import random
import math

pygame.display.init()
pygame.mixer.init()
#load = pygame.mixer.music.load(11408^LASER1.mp3)
#play = pygame.mixer.music.play(load)
screenx = 800
screeny = 600
screen = pygame.display.set_mode((screenx,screeny))
clock = pygame.time.Clock()
done = False
draw_screen = False
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
playerx = 200
playery = 300
rad = 20
speed = 150
clist = []

while not done:
    #Update
    dt = clock.tick() / 1000.0
    if playerx <= 20:
        playerx = 20
    if playerx >= 780:
        playerx = 780
    if playery <= 20:
        playery = 20
    if playery >= 580:
        playery = 580

    #Input
    queue = pygame.event.get()
    mPress = pygame.mouse.get_pressed()
    kPress = pygame.key.get_pressed()
    mx,my = pygame.mouse.get_pos()
    if kPress[pygame.K_ESCAPE]:
        done = True
    if kPress[pygame.K_w]:
        playery -= speed * dt
    if kPress[pygame.K_s]:
        playery += speed * dt
    if kPress[pygame.K_a]:
        playerx -= speed * dt
    if kPress[pygame.K_d]:
        playerx += speed * dt
    for e in queue:
        if e.type == pygame.MOUSEBUTTONDOWN:
            draw_screen = True
    #Draw
    #screen.fill(black)
    if draw_screen == True:
         random_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
         screen.fill(random_color)
         #play
         draw_screen = False
    #Draw Player
    pygame.display.flip()

pygame.mixer.quit()
pygame.display.quit()
