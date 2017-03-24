import math
import pygame
import math3d
import random
import time

class PBody(object):
    """Physics based"""
    def __init__(self, pos, coeff = 1, weight=10, mass=1.0, vel=(0,0)):
        self.pos = math3d.VectorN(pos)
        self.vel = math3d.VectorN(vel)
        self.rad = 10
        self.bullet_rad = 5
        self.force = math3d.VectorN((5,5))
        self.grey = (211,211,211)
        self.white = (255,255,255)
        self.red = (255,0,0)
        #Below is used for terminal velocity
        self.mass = mass
        self.weight = weight
        self.coeff = coeff
        #Above is used for terminal velocityS
        self.magx = 750
        self.magy = 50
        self.circle_pos = self.pos.toIntTuple()
        self.circle_list = []
        self.bullets = []
        self.bullet_locx = playerx + 5
        self.bullet_locy = playery + 5

    def render(self,surf):
        """Draws circle to surf """
        for i in range(15):
            pygame.draw.circle(surf,self.white,self.circle_pos,self.rad)
            PBodylist.append([self.circle_pos])

    def update(self, dT):
        """Updates the object
           1. Change position due to current velocity
           2. Apply friction (optional).
           3. Enforce a terminal velocity (optional). """
        #1. Change the players position
        self.pos += self.vel * dT
        #2. Friction
        friction = self.pos - self.vel * dT
        #-k * vel/||vel||
        #3. Terminal velocity
        termV = (float(2*self.weight)/float(self.coeff*20*10))**0.5


    def applyForce(self, F, dT):
        """Handles velocity and accelleration of the PBody"""
        a = F / self.mass #Where a is the body's accelleration

    def magnetism(self, surf, magx, magy):
        """Draws a square and lets PBody's move towards it"""
        PBody.render(self,surf)
        pygame.draw.square(surf, self.red,(magx,magy,5,5),1)
        vectorpi = math3d.VectorN(self.x,self.y)
        vectorpm =math3d.VectorN(x,y)
        normalpvector1 = math3d.VectorN.normalized_copy(vectorpi)
        normalpvector2 = math3d.VectorN.normalized_copy(vectorpm)
        magpi = math3d.VectorN.magnitude(vectorpi)
        magpm = math3d.VectorN.magnitude(vectorpm)

        Fm = (self.mass / (magpi - magpm)**2) * (normalpvector1 - normalpvector2)

    def fire(self):
        """ Create a new PBody in self.bullets.  Give it the position of
            the front of the snow-mobile and a velocity based on the draw-
            direction you might be able to use math3d.polar_to_cartesian here). """
        math3dsol.VectorN.polar_to_cartesian(15,self.draw_angle)
        bullet_locx = playerx + 5
        bullet_locy = bullet_locx
        for e in pygame.event.get:
            if event.type == kPress[pygame.K_SPACE]:
                self.bullets.append([bullet_locx,bullet_locy])

    def redline(self,surf):
        """Draws the lines for an interior obstacle"""
        pygame.draw.lines(surf, self.red, True, [0,20], [5,450], [700,450], [700,20])


class Player(PBody):
    def loadimage(self, fname):
        """Loads the image of the snowmobile:
            The fname is a string of the image path"""
        self.surf = pygame.image.load(fname)
        self.draw_angle = 0 #Direction that the player is facing, in degrees
        self.bullets = []

    def moveTowards(self,fwd_back,left_right,dT):
        """Points the player snowmobile towards a position using WASD keys"""
        applyForce(player_speed_f,dT)
        k = 50
        movx,movy = math3dsol.VectorN.polar_to_cartesian(k,self.draw_angle)
        if player_speed > 50:
            F = (k * fwd_back) + (k * left_right)
        else:
            F = (k * fwd_back)

    def render(self, surf):
        """Draw the image and rotate it appropriately"""
        PBody.render(self, surf)
        tempS = pygame.transform.rotate(self.surf,self.draw_angle)

    def update(self, dT):
        """Updates the PBody"""
        PBody.update(self, dT)
        #Simple wall bouncing (player)
        if self.pos[0] > 750:
            self.pos[0] = 750
        if self.pos[1] > 550:
            self.pos[1] = 550
        if self.pos[0] < 50:
            self.pos[0] = 50
        if self.pos[1] < 50:
            self.pos[1] = 50
        # Bullet check
        for bullet in self.bullets:
            if bullet_locx >= 800:
                self.bullets.remove(bullet)
            if bullet_locy >= 600:
                self.bullets.remove(bullet)
            if bullet_locx or bullet_locy <= -1:
                self.bullets.remove(bullet)


pygame.display.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
playerx = 150
playery = 300
fill = 0
black = (0,0,0)
B = PBody((400,300), 1.0)
player_speed_f = math3d.VectorN((5,5,0))
player_speed = B.applyForce(player_speed_f,dT)
Player.loadimage(b4_top.png)#from the destop or .zip folder

while not done:
    # UPDATE
    dT = clock.tick() / 1000.0
    B.applyForce(math3d.VectorN(0,10), dT)
    B.update(dT)     # Call (only) ONCE per frame
    Player.update(dT)

    # INPUT
    Event = pygame.event.get()
    kPress = pygame.key.get_pressed()
    mPress = pygame.mouse.get_pressed()
    mPos = pygame.mouse.get_pos()
    for event in Event:
        if event.type == pygame.KEYDOWN:

            if e.key == pygame.K_w:
                playery -= player_speed
            if e.key == pygame.K_a:
                playerx -= player_speed
            if e.key == pygame.K_s:
                playery += player_speed
            if e.key == pygame.K_d:
                playerx += player_speed
            if e.key == pygame.K_ESCAPE:
                pygame.display.quit()

    # DRAW
    screen.fill(black)
    B.render(screen)
    for bullet in B.self.bullets:
        pygame.draw.circle(surf,self.white,(B.bullet_locx,B.bullet_locy),B.bullet_rad)
    pygame.display.flip()
pygame.display.quit()