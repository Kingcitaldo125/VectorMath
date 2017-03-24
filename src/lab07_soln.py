import math3d

class Scene(object):
    def __init__(self, renderSurf):
        """ Initializes the surface this scene will
            be rendered to. """
        self.surf = renderSurf

    def setCamera(self, camPos, camCOI, camUp, camNear=1.5):
        """ Set up camera space. """
        self.camPos = camPos   # Origin of camera space
        self.camNear = camNear
        self.camZ = (self.camPos - camCOI).normalized_copy()
        self.camX = math3d.cross(camUp, self.camZ).normalized_copy()
        self.camY = math3d.cross(self.camZ, self.camX)   # camZ and camX are
                                                         # perpendicular and unit_length, so
                                                         # the result is unit-length.  This
                                                         # wasn't the case when constructing
                                                         # camX and camZ
        print("self.camX = " + self.camX.stringFormatted(4)) # A utility function I made in math3d.
        print("self.camY = " + self.camY.stringFormatted(4))
        print("self.camZ = " + self.camZ.stringFormatted(4))

    def cameraToWorld(self, p):
        """ P is a point defined relative to camera space.
            This method returns an equivalent definition of
            P relative to WORLD space. Hint: use slide 7 or 8
            in lecture 7 (you figure out which you need -- you
            won't need both) """
        result = self.camPos
        result += p[2] * self.camZ     # result is now in the middle of the view-plane
        result += p[0] * self.camX     # result is now in the middle-left of the view-plane
        result += p[1] * self.camY     # result is now the world-space equivalent of p
        return result

    def screenToCamera(self, x, y):
        """ (x, y) is a PYGAME coordinate.  Your job is
            to convert this to an equivalent point on the
            virtual view screen (in CAMERA SPACE).  Make sure
            this always works with whatever screen (surface)
            size you currently have. """
        cx = x / (self.surf.get_width() - 1) - 0.5
        cy = y / (self.surf.get_height() - 1)
        cy = (1.0 - cy) - 0.5         # Flips the y-axis from pygame.
        return math3d.VectorN((cx, cy, -self.camNear))


if __name__ == "__main__":
    import pygame

    pygame.display.init()
    pygame.mouse.set_visible(False)
    win_width = 600;   win_height = 600
    screen = pygame.display.set_mode((win_width, win_height))



    S = Scene(screen)
    camera_pos = math3d.VectorN((5,-1,7))
    camera_coi = math3d.VectorN((0,15,-2))
    camera_up = math3d.VectorN((0,1,0))
    S.setCamera(camera_pos, camera_coi, camera_up)

    # some unit tests (new)
    tests = [(0,0), (599,0), (0,599), (599,599), (300,100), (42,37)]
    for t in tests:
        c = S.screenToCamera(t[0], t[1])
        w = S.cameraToWorld(c)
        print("pygame" + str(t))
        print("\tcamera = " + c.stringFormatted(4))
        print("\tworld = " + w.stringFormatted(4))

    while True:
        # Input
        pygame.event.get()
        kPress = pygame.key.get_pressed()
        mPos = pygame.mouse.get_pos()

        # (commented for testing above cases)
        cameraPos = S.screenToCamera(mPos[0], mPos[1])
        worldPos = S.cameraToWorld(cameraPos)
        print(worldPos)

        if kPress[pygame.K_ESCAPE]:
            break

        # Draw
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (255,255,255), mPos, 5)
        pygame.display.flip()
    pygame.display.quit()