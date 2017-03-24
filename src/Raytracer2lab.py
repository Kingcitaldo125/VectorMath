import math3d
import math
import random

class Scene(object):
    def __init__(self, renderSurf):
        """Initializes the surface this scene will
            be rendered to. """
        self.surf = renderSurf
        self.aspectR = self.surf.get_width() / self.surf.get_height()
        self.obj_list = []

    def setCamera(self, camPos, camCOI, camUp, camNear, cameravertFOV):
        """Set up camera space. """
        self.camPos = camPos   # Origin of camera space
        self.camNear = 1.5
        self.camCOI = camCOI
        self.camUp = camUp
        self.newcameravertFOV = cameravertFOV / 2
        self.viewHeight = self.camNear * math.tan(self.newcameravertFOV)
        self.viewWidth = self.camNear
        virtualaspectR = self.viewWidth/ self.viewHeight
        Q = math3d.VectorN.__sub__(self.camPos,self.camCOI)
        #Normalized copy of camera pos
        self.norm_copy = math3d.VectorN.normalized_copy(Q)
        self.camz = self.norm_copy
        self.camx = math3d.cross(self.camz,self.camUp)
        self.camy = math3d.cross(self.camz,self.camx)
        math3d.VectorN.normalized_copy(self.camx)
        math3d.VectorN.normalized_copy(self.camy)
        math3d.VectorN.normalized_copy(self.camz)
        return self.camx, self.camy, self.camz

    def cameraToWorld(self, p):
        """P is a point defined relative to camera space.
            This method returns an equivalent definition of
            P relative to WORLD space. Use slide 7 and 8 lecture 7 for this part."""
        print(p,"Camera space point")
        result = self.camPos
        print(self.camPos)
        result += self.camx     # result is now in the middle of the view-plane
        result += self.camy     # result is now in the middle-left of the view-plane
        result += self.camz       # result is now the world-space equivalent of p
        return result

    def screenToCamera(self, x, y):
        """(x, y) is a PYGAME coordinate.  Your job is
            to convert this to an equivalent point on the
            virtual view screen (in CAMERA SPACE) Use slides 7 and 8 in lecture 7 """
        #self.x = x
        #self.y = y
        new_x = (x / self.surf.get_width()) - self.viewWidth/2
        new_y = (y / self.surf.get_height())
        new_y = (1.0 - new_y) - self.viewHeight / 2
        new_z = -self.camNear
        formula = math3d.VectorN((new_x,new_y,new_z))
        return formula

    def renderOneLine(self, py):
        """Renders one horizontal line of the pygame window, eventually showing the
            fully rendered image"""
        px = 0
        world_px = S.cameraToWorld(px)
        world_py = S.cameraToWorld(py)
        world_camz = S.cameraToWorld(self.camz)
        while px <= 9:
            print("Pixel: " + "(" + str(px) + ", " + str(py) + ") " + "= " + " " +
                 str(math3d.VectorN((world_px,world_py,self.camz))) + " " + "(world)")
            px+=1

    def addObject(self, obj):
        """Adds object to the list of objects"""
        self.obj_list.append(obj)

if __name__ == "__main__":
    import pygame

    pygame.display.init()
    pygame.mouse.set_visible(False)
    win_width = 10
    win_height = 7
    screen = pygame.display.set_mode((win_width, win_height))
    S = Scene(screen)
    camera_pos = math3d.VectorN((6,2,20))
    camera_coi = math3d.VectorN((-3,0,0))
    camera_up = math3d.VectorN((0,1,0))
    camera_near = 2.3
    cameravertFOV = 75 #degrees
    S.setCamera(camera_pos, camera_coi, camera_up, camera_near, cameravertFOV)
    render_linenum = 0

    while True:
        # Update

        # Input
        pygame.event.get()
        kPress = pygame.key.get_pressed()
        mPress = pygame.mouse.get_pressed()
        pygame.event.get()
        if kPress[pygame.K_ESCAPE]:
            break

        # Draw
        #screen.fill((0,0,0))
        #pygame.draw.circle(screen, (255,255,255), mPos, 5)
        while render_linenum < win_height:
            S.renderOneLine(render_linenum)
            render_linenum+=1
        pygame.display.flip()
    pygame.display.quit()