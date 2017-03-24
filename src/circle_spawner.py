import random
import pygame
import time

pygame.display.init()
winx = 800
winy = 600

Screen = pygame.display.set_mode((winx,winy))
Circles = []

def spawn():
    """Also could be considered the input..."""
    ranx = random.randrange(1,winx)
    rany = random.randrange(1,winy)
    kPress = pygame.key.get_pressed()
    mPress = pygame.mouse.get_pressed()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Circles.append([ranx,rany])

    #def update(self):
     #   """ """

def draw():
    """ """
    black = (0,0,0)
    color = (255,0,0)
    rad = 5
    Screen.fill(black)
    for i in Circles:
        pygame.draw.circle(Screen,color,(i[0],i[1]),rad)
        print(i)
    pygame.display.flip()

def main():
    """ """
    while True:
        #update()
        spawn()
        draw()

if __name__ == '__main__':main()