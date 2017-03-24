import math3d
import math
import objects3d

class Light(object):
    def __init__(self,pos,diff,spec):
        """Holds the pos,and material values for each light"""
        self.pos = pos
        self.diff = diff
        self.spec = spec
        self.lights = []

    def equation(self):
        """Calculates and returns the lighting equation for all lights and
           light materials"""
        for light in range(0,len(self.lights)):
            diff_c = Materials.diffuse(light.pos,closestObject,closestObject.result["Normal"]\
                     ,light.diff,closestObject.diff)
            light_total = light.diff + light.spec
        self.lit_c = Materials.Amb_c + light_total
        return (self.lit_c,0,1).clamped

class Materials(object):
    def __init__(self,amb,diff,spec,hard):
        """All of the material texture values will be stored here"""
        self.ambient = amb
        self.diffuse = diff
        self.specular = spec
        self.hardness = hard

class Scene(object):
    def __init__(self,renderSurf,scene_ambient):
        """ Initializes the surface this scene will
            be rendered to. """
        self.surf = renderSurf
        self.aspect = self.surf.get_width() / self.surf.get_height()
        self.grey = (64,64,64)
        self.scene_ambient = scene_ambient
        self.objects = []                    # The list of renderables in the scene
        self.lights = []

    def setCamera(self, camPos, camCOI, camUp, camNear, vertFov):
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
        #print("viewHeight = " + str(self.viewHeight))
        #print("viewWidth = " + str(self.viewWidth))

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
        """Adds object to the object list"""
        self.objects.append(o)

    def addLight(self, l):
        """Adds a new light to a list of lights"""
        self.lights.append(l)

    def getLitColor(self,t,N,pt,amb,diff,spec,hard):
        """Takes: the hit object,normal,intersection point,amb,diff,spec,hardness
           and returns lit / shaded color"""
        self.ambient = amb
        self.diffuse = diff
        self.specular = spec
        self.hard = hard
        self.N = N.normalized_copy()
        #Calculate a diffuse color for each light
        for light in range(0,Light.lights):
            lDirdiff = light[0] - t
            lDirHatdiff = lDirdiff / lDirdiff.magnitude()
            dStrdiff = math3d.dot(lDirHatdiff,self.N)
            if dStrdiff <= 0:
                cDiff = math3d.VectorN((0,0,0))
            else:
                cDiff = dStr*(math3d.pairwise(light[1],self.diffuse))
        #Calculate a Specular color for each light
        for light in range(0,Light.lights):
            lDirspec = light[0] - t
            lDirHatspec = lDirHatspec / lDirHatspec.magnitude()
            Rvector = 2*(math3d.dot(lDirHatspec,self.N)*(self.N - lDirHatspec))
            Vvector = (setCamera.camPos) - (t)
            Vhat = Vvector/Vvector.magnitude()
            sStr = math3d.dot(Vhat,Rvector)
            if sStr <= 0:
                cSpec = math3d.VectorN((0,0,0))
            else:
                cSpec = sStr*(math3d.pairwise(light[1],self.specular))
            #ray_origin = t + .00001
            #ray_dir = math3d.normalized_copy((light - t))
            #shad_ray = objects3d.Ray(ray_origin,ray_dir,None)
            #for o in range(0,len(self.objects)):
             #   result = o.rayHit(light_ray)
              #  if result != None:
               #     self.cLit = self.ambient
                #else:
                 #   self.cLit = self.ambient + (cDiff + cSpec)

        return self.cLit

    def renderOneLine(self, y):
        for x in range(0, self.surf.get_width()):
            camSpace = self.screenToCamera(x, y)
            worldSpace = self.cameraToWorld(camSpace)
            origin = worldSpace
            dreg = math3d.VectorN.normalized_copy((worldSpace - self.camPos))
            # Step1. Create a ray.
            new_ray = objects3d.Ray(origin, dreg, None)
            #math3d.VectorN.normalized_copy((worldSpace - self.camPos)))

            closestObject = None
            closestT = None
            closestP = None
            closestN = None
            obj_list = []
            tlist = []

            for o in range(0,len(self.objects)):
                result = self.objects[o].rayHit(new_ray)
                if result != None:
                    for i in range(len(result["tlist"])):
                        t = result["tlist"][i]
                        p = result["plist"][i]
                        N = result["Normal"][i]
                        if t > 0:
                            tlist.append(t)
                            for i in range(len(tlist)):
                                if closestT == None:
                                    closestT = t
                                    closestObject = self.objects[o]
                                    closestP = p
                                    closestN = N
                                if t < closestT:
                                    closestT = t
                                    closestObject = self.objects[o]
                                    closestP = p
                                    closestN = N

            if closestObject == None:
                self.surf.set_at((x,y),(64,64,64))
            else:
                #            Try with either CLosest T or Closest P V V V
                color = (Scene.getLitColor(closestObject,closestN,closestP,\
                (closestObject.RedMat,closestObject.GreenMat,closestObject.BlueMat)))
                self.surf.set_at((x,y),color)

if __name__ == "__main__":
    import pygame

    pygame.display.init()
    pygame.mouse.set_visible(False)
    win_width = 500;   win_height = 300
    screen = pygame.display.set_mode((win_width, win_height))


    ambient_vector = math3d.VectorN((1,1,1))
    S = Scene(screen,ambient_vector)
    camera_pos = math3d.VectorN((6,14,10))
    camera_coi = math3d.VectorN((-3,5,0))
    camera_up = math3d.VectorN((0,1,0))
    camera_near = 1.5
    camera_FOV = 60.0 #degrees
    S.setCamera(camera_pos, camera_coi, camera_up, camera_near, camera_FOV)
    S.scene_ambient = math3d.VectorN((1,1,1))

    blueM = Materials([0.1,0.3,0.3],[0.3,0.4,1.0],[0.4,0.4,0.4],5.0)
    greenM = Materials([0,0.3,0],[0,1,0],[0,0,1],10.0)
    redM = Materials([0.3,0,0],[1,0,0],[1,1,0],10.0)
    purpleM = Materials([0.3,0,0.3],[0.8,0,1],[1,1,1],20.0)
    yellowM = Materials([0.3,0,0.3],[0.8,0,1],[1,1,1],20.0)
    # INCLUDE FOR TRIANGLE MESH

    # 5 objects
    #ambient,specular diffuse and hardness should also be passed: S.addObject(objects3d.Plane(math3d.VectorN((0,1,0)),)
    S.addObject(objects3d.Box(math3d.VectorN((-5,1,0)), math3d.VectorN((-14,10,-5)),(greenM)))
    #color = (0,255,0))) #0

    S.addObject(objects3d.Sphere1(math3d.VectorN((0,5,0)), 4.0, (redM)))
    #color = (255,0,0))) #1 Sphere Number 1

    S.addObject(objects3d.Sphere2(math3d.VectorN((3,15,-3)), 6.0,(redM,blueM)))
    #color = (51,0,25))) #2 Sphere Number 2

    S.addObject(objects3d.Plane(math3d.VectorN((0,1,0)), 0.0,(blueM)))
    #color = (100,100,255))) #3

    S.addObject(objects3d.Triangle(math3d.VectorN((5,2,-10)), math3d.VectorN((16,2,-7)), math3d.VectorN((12,11,-15)),\
    (redM,greenM))) #color = (255,100,255))) #4

    #S.addObject(objects3d.TriangleMesh("monkey_smooth.obj", 3.5, [-10,4,6],\
    #(RedMat,GreenMat,BlueMat))) #color = (255,0,0) #5

    S.addLight((math3d.VectorN((10, 50, 10)), math3d.VectorN((1, 1, 1)), math3d.VectorN((1, 1, 1))))
    S.addLight((math3d.VectorN((0, 45, -40)), math3d.VectorN((0.4, 0, 0)), math3d.VectorN((0.6, 0.9, 0.6))))
    curY = 0
    #print(S.objects)

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