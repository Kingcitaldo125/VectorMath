import math3d

def setCamera(self, camPos, camCOI, camUp, camNear=1.5):
        """ Set up camera space. """
        self.camPos = camPos   # Origin of camera space
        self.camNear = camNear
        self.camCOI = camCOI
        Q = math3d.VectorN.__sub__(self.camPos,self.camCOI)
        #Normalized copy of camera pos
        self.norm_copy = math3d.VectorN.normalized_copy(self.camPos)
        self.camx = 1
        self.camz = math3d.VectorN.__neg__(Q)
        self.camy = math3d.cross(self.camz,Q)
        return self.camx, self.camy, self.camz

camera_pos = math3d.VectorN((5,-1,7))
camera_coi = math3d.VectorN((0,15,-2))
camera_up = math3d.VectorN((0,1,0))
camera_near = 1.5
setCamera(camera_pos, camera_coi, camera_up, camera_near)