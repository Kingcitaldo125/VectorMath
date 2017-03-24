import math3d
import math
import pygame
import random


class PBody(object):
    """ A physics-enabled object. """
    def __init__(self, pos, mass=1, rad=10, vel=(0,0), color=(255,255,255)):
        self.pos = math3d.VectorN(pos)
        self.vel = math3d.VectorN(vel)
        self.rad = 10                    # in pixels
        self.color = color
        self.mass = mass

    def render(self, surf):
        pygame.draw.circle(surf, self.color, \
                          self.pos.toIntTuple(), self.rad)

    def update(self, dT):
        """ Updates our object:
            1. Changes position due to current velocity.
            2. (optional) Apply friction
            3. (optional) Enforce a terminal velocity
        """
        self.pos += self.vel * dT

    def applyForce(self, F, dT):
        """ Modify velocity such that we apply the FORCE
            f for dT seconds.  Note: F = ma """

class Player(PBody):
    def loadImage(self, file_name):
        """ file_name is a string (of the image path / filename)
            e.g. 'b4_top.png' or 'imgs\\b4_top.png' """
        self.surf = pygame.image.load(file_name)
        self.draw_angle = 0      # In degrees
        self.bullets = []

    def moveTowards(self, mx, my):
        """ Makes the player accelerate towards the mouse.  Note:
            this will call self.applyForce. """
        pass

    def fire(self):
        """ Create a new PBody in self.bullets.  Give it the position of
            the front of the snow-mobile and a velocity based on the draw-
            direction you might be able to use math3d.polar_to_cartesian here). """

    def update(self, dT):
        # Call the base-class (PBody) update first
        PBody.update(self, dT)

        # Do the player-specific updates here.  e.g. update all bullets and remove
        # "dead" ones.

    def render(self, surf):
        PBody.render(self, surf)   # Call base-class render

        # Draw the snowmobile image (or some other image),
        # rotated (and centered) appropriately.
        tempS = pygame.transform.rotate(self.surf, self.draw_angle)


pygame.display.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False

B = PBody((400,300), 1)


while not done:
    # Update
    deltaTime = clock.tick() / 1000.0

    B.applyForce(math3d.VectorN(0,10), deltaTime)   # Called ONCE per frame to apply gravity.
    B.update(deltaTime)     # Called ONCE per frame

    # Input
    pygame.event.get()
    kPress = pygame.key.get_pressed()
    mPress = pygame.mouse.get_pressed()
    mPos = pygame.mouse.get_pos()
    if kPress[pygame.K_ESCAPE]:
        done = True

    # Draw
    screen.fill((0,0,0))
    B.render(screen)

    pygame.display.flip()
pygame.display.quit()

