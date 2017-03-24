import math3d
import math

class Scene(object):
    def __init__(self, renderSurf):
        """ Initializes the surface this scene will
            be rendered to. """
        self.surf = renderSurf
        self.aspect = self.surf.get_width() / self.surf.get_height()
        self.objects = []                    # The list of renderables in the scene

    def setCamera(self, camPos, camCOI, camUp, camNear=1.5, vertFov=60.0):
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
        self.viewHeight = 2.0 * self.camNear * math.tan(math.radians(vertFov / 2.0))
        self.viewWidth = self.aspect * self.viewHeight
        print("viewHeight = " + str(self.viewHeight))
        print("viewWidth = " + str(self.viewWidth))

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
        cx = self.viewWidth * (x / (self.surf.get_width() - 1) - 0.5)
        cy = self.viewHeight * (y / (self.surf.get_height() - 1) - 0.5)
        return math3d.VectorN((cx, -cy, -self.camNear))


    def addObject(self, o):
        self.objects.append(o)


    def renderOneLine(self, y):
        for x in range(0, self.surf.get_width()):
            camSpace = self.screenToCamera(x, y)
            worldSpace = self.cameraToWorld(camSpace)
            print("Pixel(" + str(x) + ", " + str(y) + ") = " + str(worldSpace) + " (world)")



if __name__ == "__main__":
    import pygame

    pygame.display.init()
    pygame.mouse.set_visible(False)
    win_width = 10;   win_height = 7
    screen = pygame.display.set_mode((win_width, win_height))



    S = Scene(screen)
    camera_pos = math3d.VectorN((6,2,20))
    camera_coi = math3d.VectorN((-3,0,0))
    camera_up = math3d.VectorN((0,1,0))
    S.setCamera(camera_pos, camera_coi, camera_up, 2.3, 75.0)


    curY = 0

    while True:
        # Update
        if curY < win_height:
            S.renderOneLine(curY)
            curY += 1

        # Input
        pygame.event.get()
        kPress = pygame.key.get_pressed()
        if kPress[pygame.K_ESCAPE]:
            break

        # Draw
        pygame.display.flip()
    pygame.display.quit()