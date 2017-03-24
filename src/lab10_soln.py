import math3d
import math
import objects3d
import time

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
        """ Adds an object (from objects3d.py) to the list of renderables """
        self.objects.append(o)


    def renderOneLine(self, y):
        """ Fills in the colors for one row of pixels on the pygame surface
            that was given to the constructor.  This is done by creating a ray
            in virtual space for each pixel, sending it out into the world and finding the
            closest intersection point.  If such an intersection is found, the
            color of the object hit is used to color that pixel.  If no intersections
            are found, the pixel is set to a background color """
        for x in range(0, self.surf.get_width()):
            camSpace = self.screenToCamera(x, y)
            worldSpace = self.cameraToWorld(camSpace)

            # Step1. Create a ray.
            R = objects3d.Ray(worldSpace, worldSpace - self.camPos, None)

            # Step2. Test the ray against each primitive, keeping track of:
            #        a) The smallest non-negative t-value, b) The object that
            #        was hit at that distance along the ray.
            closestObject = None
            closestT = None
            # Step2a. Iterate through all primitives in self.objects (which is made
            #        up of objects like Spheres, Boxes, Triangles, etc.)
            for o in self.objects:
                result = o.rayHit(R)
                if result != None:
                    for t in result["tlist"]:
                        if t > 0 and (closestObject == None or t < closestT):
                            closestObject = o
                            closestT = t

            # Step3. If closestObject is None, set color to a background color (64,64,64),
            #        Otherwise, look at the color field of closestObject and set it to color.
            if closestObject == None:
                color = (64, 64, 64)
            else:
                color = closestObject.color
            self.surf.set_at((x, y), color)



if __name__ == "__main__":
    import pygame

    pygame.display.init()
    pygame.mouse.set_visible(False)
    win_width = 500;   win_height = 300
    screen = pygame.display.set_mode((win_width, win_height))


    # Create the scene
    S = Scene(screen)
    camera_pos = math3d.VectorN((6,2,20))
    camera_coi = math3d.VectorN((-3,0,0))
    camera_up = math3d.VectorN((0,1,0))
    S.setCamera(camera_pos, camera_coi, camera_up, 1.5, 60.0)


    # (NEW in Lab10) Add objects to render
    S.addObject(objects3d.Plane(math3d.VectorN((0,1,0)), 0.0, (100,100,255)))
    S.addObject(objects3d.Sphere(math3d.VectorN((0,0,0)), 4.0, (255,0,0)))
    #S.addObject(objects3d.Box(math3d.VectorN((-5,-4,0)), math3d.VectorN((-10,5,-5)), (0,255,0)))
    #S.addObject(objects3d.Triangle(math3d.VectorN((5,1,-10)), math3d.VectorN((12,1,-7)), math3d.VectorN((8.5, 9, -8.5)), (255,100,255)))
    #S.addObject(objects3d.TriangleMesh("monkey.obj", 1.5, (-12,0,6), (255,255,0)))

    curY = 0
    startTime = time.time()

    while True:
        # Update
        if curY < win_height:
            S.renderOneLine(curY)
            curY += 1
            if curY == win_height - 1:
                print("Elapsed time:", time.time() - startTime)

        # Input
        pygame.event.get()
        kPress = pygame.key.get_pressed()
        if kPress[pygame.K_ESCAPE]:
            break

        # Draw
        pygame.display.flip()
    pygame.display.quit()