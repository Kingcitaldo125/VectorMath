import math
import os as Operatingsys
import pygame as pg

startbet = 1
minbet = 0
maxbet = 10

def changeup(cur):
    """ """
    global startbet
    if cur == maxbet:
        assert(cur!=maxbet)
    else:
        startbet+=1
        print(startbet)

def changedown(cur):
    """ """
    global startbet
    if cur==minbet:
        assert(cur!=minbet)
    else:
        startbet-=1
        print(startbet)

pg.display.init()
screen = pg.display.set_mode((500,500))
clock = pg.time.Clock()
black=(0,0,0)

done = False
while not done:
    dt = clock.tick()/1000.0
    events = pg.event.get()

    for e in events:
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_UP:
                changeup(startbet)
            if e.key == pg.K_DOWN:
                changedown(startbet)
            if e.key == pg.K_ESCAPE:
                done = True

    screen.fill(black)
    pg.display.flip()

pg.display.quit()

