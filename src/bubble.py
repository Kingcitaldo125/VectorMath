import pygame
import math
import time
import random

winx=800
winy=600

class Bubble(object):
    def __init__(self,x,y,r,c):
        self.x=x
        self.y=y
        self.rad=r
        self.color=c
        self.t=random.randrange(-1,1)
        self.rx=random.randrange(10,50)
        self.ry=random.randrange(10,50)
        if self.t==-1:
            self.rx*=-1
        if self.t==0:
            self.ry*=-1
        self.flag=False
        
    def update(self,mPos,dt):
        global winx,winy
        self.flag=False
        self.x+=self.rx*dt
        self.y+=self.ry*dt
        if ((mPos[0]-self.x)**2+(mPos[1]-self.y)**2)**0.5 <= self.rad+1:
            self.flag=True
        if self.x-self.rad<=0:
            self.rx*=-1
        if self.x+self.rad>=winx:
            self.rx*=-1
        if self.y-self.rad<=0:
            self.ry*=-1
        if self.y+self.rad>=winy:
            self.ry*=-1
        return self.flag
    
    def render(self,sf):
        pygame.draw.circle(sf,self.color,(int(self.x),int(self.y)),self.rad,1)

pygame.display.init()
screen = pygame.display.set_mode((winx,winy))
bs=[]
b=Bubble(random.randrange(40,760),random.randrange(40,560),40,(255,14,134))
bs.append(b)
done=False
clock = pygame.time.Clock()
while not done:
    dt=clock.tick()/1000.0
    mP = pygame.mouse.get_pos()
    if len(bs)<1:
        b=Bubble(random.randrange(40,760),random.randrange(40,560),40,(255,14,134))
        bs.append(b)
    u=b.update(mP,dt)
    events = pygame.event.get()
    for e in events:
        if e.type==pygame.MOUSEBUTTONDOWN:
            if u:
                for xs in bs:
                    bs.remove(xs)
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:
                done=True
        if e.type==pygame.QUIT:
            done=True
    screen.fill((0,0,0))
    for bb in bs:
        bb.render(screen)
    pygame.display.flip()
pygame.display.quit()
