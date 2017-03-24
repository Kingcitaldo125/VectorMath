import math3dsol

class Scene(object):
    def __init__(self, renderSurf):
        """ Initializes the surface this scene will
            be rendered to. """
        self.surf = renderSurf

    def setCamera(self, camPos, camCOI, camUp, camNear = 1.5):
        """ Set up camera space. """
        self.camPos = camPos   # Origin of camera space
        self.camNear = camNear
        self.camCOI = camCOI
        self.Q = math3dsol.VectorN.__sub__(self.camPos,self.camCOI)
        #Normalized copy of camera pos
        self.norm_copy = math3dsol.VectorN.normalized_copy(self.camPos)
        self.camz = self.Q
        self.camy = math3dsol.cross(self.camz,self.camPos)
        self.camx = math3dsol.cross(self.camy,self.camz)
        math3dsol.VectorN.normalized_copy(self.camx)
        math3dsol.VectorN.normalized_copy(self.camy)
        math3dsol.VectorN.normalized_copy(self.camz)
        return self.camx, self.camy, self.camz

    def cameraToWorld(self, p):
        """ P is a point defined relative to camera space.
            This method returns an equivalent definition of
            P relative to WORLD space. Use slide 7 and 8 lecture 7 for this part."""
        result = self.camPos
        result += p[2] * self.camZ     # result is now in the middle of the view-plane
        result += p[0] * self.camX     # result is now in the middle-left of the view-plane
        result += p[1] * self.camY     # result is now the world-space equivalent of p
        return result

    def screenToCamera(self,x,y):
        """ (x, y) is a PYGAME coordinate.  Your job is
            to convert this to an equivalent point on the
            virtual view screen (in CAMERA SPACE) Use slides 7 and 8 in lecture 7 """
        #self.x = x
        #self.y = y
        new_x = x / (self.surf.get_width() - 1) - 0.5
        #-(new_x)
        new_y = y / (self.surf.get_height() - 1)
        new_y = (1.0 - cy) - 0.5
        new_z = -self.camNear
        formula = math3dsol.VectorN((new_x,new_y,new_z))
        return formula

        # FINISH ME!!!


if __name__ == "__main__":
    import pygame

    pygame.display.init()
    pygame.mouse.set_visible(False)
    win_width = 800;   win_height = 600
    screen = pygame.display.set_mode((win_width, win_height))

    S = Scene(screen)
    camera_pos = math3dsol.VectorN((5,-1,7))
    camera_coi = math3dsol.VectorN((0,15,-2))
    camera_up = math3dsol.VectorN((0,1,0))
    camera_near = 1.5
    S.setCamera(camera_pos, camera_coi, camera_up, camera_near)
    printer = S.screenToCamera(599,599)
    print(printer)

    while True:
        # Input
        pygame.event.get()
        kPress = pygame.key.get_pressed()
        mPos = pygame.mouse.get_pos()

        cameraPos = S.screenToCamera(mPos[0], mPos[1])
        worldPos = S.cameraToWorld(cameraPos)

        if kPress[pygame.K_ESCAPE]:
            break

        # Draw
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (255,255,255), mPos, 5)
        pygame.display.flip()
    pygame.display.quit()