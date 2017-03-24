import math3d
import pygame
import math
import random


class Ray(object):
    """ A directed line segment with an origin and direction """
    def __init__(self, origin, direction, color):
        """ Origin and direction are both VectorN's (of the same
            dimension).  Direction will be normalized internally """
        self.origin = origin
        self.direction = direction.normalized_copy()
        self.color = color

    def getPoint(self, t):
        """ Returns a point which is t (scalar) units along the ray.
            Technically, negative t values aren't on the ray, but occasionally
            it is convenient to think of the ray as an infinite line """
        return self.origin + t * self.direction

    def drawPygame(self, surf):
        """ Draws a 2d projection of this ray to the given surface """
        spos = (int(self.origin[0]), int(self.origin[1]))
        epos = self.getPoint(surf.get_width() + surf.get_height())
        epos = (int(epos[0]), int(epos[1]))
        pygame.draw.circle(surf, self.color, spos, 5)
        pygame.draw.line(surf, self.color, spos, epos)

class Sphere(object):
    """ A generalized spheroid.  In 2d, this is a circle, in 3d
        a sphere, and in higher-dimensions a hyper-sphere """
    def __init__(self, center, rad, color):
        """ center: a VectorN representing the sphere's center
            rad: the (scalar) radius of the sphere
            material: an instance of one of the classes in materials.py """
        self.center = center
        self.rad = rad                     # Used in drawing
        self.radSq = self.rad * self.rad   # Used in hit-detection
        self.color = color

    def rayHit(self, R):
        """ R: a Ray object in the same dimension as this sphere.
            This method returns None if the ray doesn't hit this sphere.
            If it does, a dictionary is returned with these keys:
                "tlist": a list of scalar distance(s) along the ray to get to
                         the intersection points
                "plist": a list of VectorN's (the actual intersection points).
                         Note: This list corresponds (in order and size) to the
                         'tlist' above.
        """
        Q = self.center - R.origin
        a = math3d.dot(Q, R.direction)
        b = math3d.dot(Q, Q) - a * a
        if b >= self.radSq:
            return None
        else:
            f = (self.radSq - b) ** 0.5
            t1 = a - f;             t2 = a + f
            p1 = R.getPoint(t1);    p2 = R.getPoint(t2)
            normal = (t1 - self.center).normalize()
            result = {}
            result["tlist"] = [t1, t2]
            result["plist"] = [p1, p2]
            if t1 < t2:
                result["Normal"] = [(p1 - self.center).normalize()]
            else:
                result["Normal"] = [(p2 - self.center).normalize()]
            return result

    def drawPygame(self, surf):
        """ Draws a 2d projection of this sphere to the given surface """
        cpos = (int(self.center[0]), int(self.center[1]))
        pygame.draw.circle(surf, self.color, cpos, self.rad, 1)

class Plane(object):
    """ An infinite plane """
    def __init__(self, normal, dvalue, color):
        """
            normal: the normal to the plane (VectorN).  This vector is
                    normalized internally
            dvalue: the "d" value of the plane (scalar).  This is the
                    minimal distance to get to the plane from the
                    origin.
        """
        self.normal = normal.normalized_copy()
        self.d = dvalue
        self.color = color

    def rayHit(self, R):
        """ R: a Ray object in the same dimension as this Plane.
            This method returns None if the ray doesn't hit this plane.
            If it does, a dictionary is returned with these keys:
                "tlist": a list of scalar distance(s) along the ray to get to
                         the intersection points.  Note: for the
                         plane this will always be just one value.
                "plist": a list of VectorN's (the actual intersection points).
                         Note: This list corresponds (in order and size) to the
                         'tlist' above.
        """
        den = math3d.dot(R.direction, self.normal)
        if den == 0.0:
            return None
        else:
            num = self.d - math3d.dot(self.normal, R.origin)
            t = num / den
            normaled = R.getPoint(t).normalized_copy()
            return {"Normal":[normaled], "tlist":[t], "plist":[R.getPoint(t)]}

    def drawPygame(self, surf):
        """ Draws a 2d projection of this plane to the given surface """
        # Determine if the plane's normal is more horizontal or more vertical
        if abs(self.normal[0]) > abs(self.normal[1]):
            # The normal is more horizontal.  Calculate two points at the top
            # and bottom of the screen (they might be (partially) off-screen)
            h = surf.get_height() - 1
            a = (int(self.d / self.normal[0]), 0)
            b = (int((self.d - h * self.normal[1]) / self.normal[0]), h)
        else:
            # The normal is more vertical.  Calculate two points at the left
            # and right of the screen (they might be (partially) off-screen)
            w = surf.get_width() - 1
            a = (0, int(self.d / self.normal[1]))
            b = (w, int((self.d - w * self.normal[0]) / self.normal[1]))
        pygame.draw.line(surf, self.color, a, b)

class Box(object):
    """ An axis-aligned (bounding) box. """
    def __init__(self, pt1, pt2, color):
        """ pt1 and pt2: VectorN's that are on opposing sides of the
            box.
            material: an instance of one of the classes in materials.py """
        # Find the actual min / max values of the box.
        self.minPt = pt1.copy()
        self.maxPt = pt2.copy()
        for i in range(self.minPt.mDim):
            if pt2[i] < self.minPt[i]:
                self.minPt[i] = pt2[i]
            if pt1[i] > self.maxPt[i]:
                self.maxPt[i] = pt1[i]

        # Calculate the bounding planes for the sides of the box
        self.planes = []                    # The plane bounding the 6 sides of the box (in 3d).
                                            # This code should work in any dimension.
        self.other_dim = []         # The "other" dimension to check.  When we have a hit
                                    # with a plane bounding a side, we need to ensure
                                    # that intersecion happens within the bounds of the box.  To check
                                    # this, we look at the other primary dimensions of the box.  For example,
                                    # if we're in 3d and hit the right plane (primary direction is x), we check
                                    # the y and z values to ensure they are within the range
                                    # of y values and z values in the min and max point.
        for i in range(self.minPt.mDim):
            normal = math3d.VectorN(self.minPt.mDim)

            # Positive-facing along axis i
            normal[i] = 1.0
            d = self.maxPt[i]
            self.planes.append(Plane(normal, d, None))

            # Negative-facing along axis i
            normal[i] = -1.0
            d = -self.minPt[i]
            self.planes.append(Plane(normal, d, None))

            # Build up a list of the axes != i
            other_list = []
            for j in range(self.minPt.mDim):
                if j  != i:
                    other_list.append(j)
            self.other_dim.append(other_list)
            self.other_dim.append(other_list)

        # Set the material
        self.color = color

    def rayHit(self, R):
        """ R: a Ray object in the same dimension as this box.
            This method returns None if the ray doesn't hit this box.
            If it does, a dictionary is returned with these keys:
                "tlist": a list of scalar distance(s) along the ray to get to
                         the intersection points
                "plist": a list of VectorN's (the actual intersection points).
                         Note: This list corresponds (in order and size) to the
                         'tlist' above.
        """

        epsilon = 0.00001               # To prevent numerical round-off
        tlist = []
        plist = []
        for i in range(len(self.planes)):
            p = self.planes[i]
            # First see if we hit the infinite plane bounding this side
            result = p.rayHit(R)
            if result != None:
                # If we do, inspect the intersection point and determine
                # if it's in the bounds of the other primary axes of the box.
                t = result["tlist"][0]
                p = result["plist"][0]
                in_bounds = True
                for j in self.other_dim[i]:
                    if p[j] < self.minPt[j] - epsilon or p[j] > self.maxPt[j] + epsilon:
                        in_bounds = False
                        break
                if in_bounds:
                    # Hits the box side.
                    tlist.append(t)
                    plist.append(p)
        if len(tlist) > 0:
            normaled = R.getPoint(p).normalized_copy()
            return {"Normal":normaled, "tlist":tlist, "plist":plist}

    def drawPygame(self, surf):
        """ Draws a 2d projection of this box to the given surface """
        r = (int(self.minPt[0]), int(self.minPt[1]), \
             int(self.maxPt[0] - self.minPt[0]), \
             int(self.maxPt[1] - self.minPt[1]))
        pygame.draw.rect(surf, self.color, r, 1)

class Triangle(object):
    """ A triangle """
    def __init__(self, p1, p2, p3, color):
        """ p1, p2, and p3 are 3 (non-equal) VectorN positions
            material: an instance of one of the classes in materials.py """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        # These relate to the plane the triangle lies upon.
        self.normal = math3d.cross(p2 - p1, p3 - p1)
        self.area = self.normal.magnitude()             # Technically 2x the area; speeds up barycentric test, though.
        self.normalnew = self.normal.normalized_copy()
        self.plane = Plane(self.normal, math3d.dot(p1, self.normal), None)
        self.color = color

    def rayHit(self, R):
        """ R: a Ray object in the same dimension as this triangle.
            This method returns None if the ray doesn't hit this triangle.
            If it does, a dictionary is returned with these keys:
                "tlist": a list of scalar distance(s) along the ray to get to
                         the intersection points
                "plist": a list of VectorN's (the actual intersection points).
                         Note: This list corresponds (in order and size) to the
                         'tlist' above.
        """
        result = self.plane.rayHit(R)
        if result != None:
            p = result["plist"][0]
            b1 = math3d.cross(p - self.p2, p - self.p3).magnitude()
            b2 = math3d.cross(p - self.p1, p - self.p3).magnitude()
            b3 = math3d.cross(p - self.p1, p - self.p2).magnitude()
            normalp = p.normalized_copy()
            Normal = [self.normalnew.toIntTuple()]
            if b1 + b2 + b3 > self.area + 0.001:
                result = None
        return result

    def drawPygame(self, surf):
        """ Draws a 2d projection of this triangle to the given surface """
        p1 = (int(self.p1[0]), int(self.p1[1]))
        p2 = (int(self.p2[0]), int(self.p2[1]))
        p3 = (int(self.p3[0]), int(self.p3[1]))
        pygame.draw.polygon(surf, self.color, (p1, p2, p3), 1)

class TriangleMesh(object):
    """ A collection of 3d triangles (loaded from a wavefront .obj file) """
    def __init__(self, fname, scale, offset, color):
        """ fname: (string) filename of a wavefront .obj file
            scale: (scalar) the amount to scale each vertex by
            offset: (tuple / Vector3) an offset to add to each vertex
            material: an instance of one of the classes in materials.py """
        vlist = []
        self.tri_list = []
        min_pt = None
        max_pt = None
        self.color = color

        # Load the file and process each line.  In addition, track the
        # min / max value (to make a bounding box)
        fp = open(fname, "r")
        if fp:
            for line in fp:
                line = line.strip()
                if len(line) == 0:
                    continue
                elif line[0] == 'v':
                    vals = line.split(" ")
                    v = math3d.VectorN((vals[1], vals[2], vals[3])) * scale + math3d.VectorN(offset)
                    if min_pt == None:
                        min_pt = v.copy()
                        max_pt = v.copy()
                    else:
                        if v[0] < min_pt[0]:    min_pt[0] = v[0]
                        if v[1] < min_pt[1]:    min_pt[1] = v[1]
                        if v[2] < min_pt[2]:    min_pt[2] = v[2]
                        if v[0] > max_pt[0]:    max_pt[0] = v[0]
                        if v[1] > max_pt[1]:    max_pt[1] = v[1]
                        if v[2] > max_pt[2]:    max_pt[2] = v[2]
                    vlist.append(v)
                elif line[0] == 'f':
                    indicies = line.split(" ")
                    p1 = vlist[int(indicies[1]) - 1]
                    p2 = vlist[int(indicies[2]) - 1]
                    p3 = vlist[int(indicies[3]) - 1]
                    self.tri_list.append(Triangle(p1, p2, p3, self.color))
            fp.close()

        # Actually create the bounding box.
        self.bounding_box = Box(min_pt, max_pt, None)

    def rayHit(self, R):
        """ R: a Ray object in the same dimension as this triangle-mesh.
            This method returns None if the ray doesn't hit this triangle.
            If it does, a dictionary is returned with these keys:
                "tlist": a list of scalar distance(s) along the ray to get to
                         the intersection points
                "plist": a list of VectorN's (the actual intersection points).
                         Note: This list corresponds (in order and size) to the
                         'tlist' above.
            Note: This method is slightly optimized by first testing
                  the ray against a containing box.
        """
        result = self.bounding_box.rayHit(R)
        if result:
            tlist = []
            plist = []
            for t in self.tri_list:
                result = t.rayHit(R)
                if result:
                    tlist.append(result["tlist"][0])
                    plist.append(result["plist"][0])
            if len(tlist) > 0:
                return {"Normal":plist.normalized_copy(), "tlist":tlist, "plist":plist}

    def drawPygame(self, surf):
        """ Draws a 2d projection of this triangle mesh to the given surface """
        for t in self.tri_list:
            t.drawPygame(surf)
