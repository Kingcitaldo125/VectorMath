import math
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@ VECTORN class                      @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class VectorN(object):
    """ This is a class which will be used to represent a vector (or a point
        in n-dimensional space. It is basically acts as a python list (of
        floats), but with extra vector operations that python lists don't
        have. """

    def __init__(self, p):
        """ The constructor.  p can be one of these type of objects:
            an integer: the dimension this vector exist in
            a sequence-like object: the values of the vector (we infer
            the dimension based on the length of the sequence """
        if isinstance(p, int):
            self.mDim = p
            self.mData = [0.0] * p
        elif hasattr(p, "__len__") and hasattr(p, "__getitem__"):
            self.mDim = len(p)
            self.mData = []
            for i in range(len(p)):
                self.mData.append(float(p[i]))
        else:
            raise TypeError("Invalid parameter.  You must pass a sequence or an integer")

    def __add__(self, rhs):
        """ Returns the vector sum of self and rhs (which must be a VectorN) """
        if not isinstance(rhs, VectorN) or self.mDim != rhs.mDim:
            raise TypeError("You can only add another Vector" + str(self.mDim) \
                            + " to this Vector" + str(self.mDim))
        c = self.copy()
        for i in range(rhs.mDim):
            c[i] += rhs[i]
        return c

    def __getitem__(self, index):
        """ Returns an element of mData """
        return self.mData[index]

    def __len__(self):
        """ Returns the dimension of this VectorN when a VectorN is passed to
           the len function (which is built into python) """
        return self.mDim

    def __mul__(self, rhs):
        """ Python passes the right-hand-side of the * operator to this method.
            It needs to be a scalar (int or float).  The method returns the
            vector product """
        if not isinstance(rhs, int) and not isinstance(rhs, float):
            raise TypeError("You can only multiply a vector by a scalar")
        new_data = []
        for val in self.mData:
            new_data.append(val * rhs)
        return VectorN(new_data)

    def __neg__(self):
        """ Returns the vector negation of self.  This is triggered by a line
            like z = -v in python """
        c = self.copy()
        for i in range(c.mDim):
            c[i] = -c[i]
        return c

    def __rmul__(self, lhs):
        """ Python calls this if __mul__ fails (usually when a non-VectorN is on
            the left-hand-side of the * operator.  Since vector-scalar multiplication
            is commutative, just return the result of self * lhs which will
            call our __mul__ method. """
        return self * lhs

    def __setitem__(self, index, value):
        """ Sets the value of self.mData[index] to value """
        self.mData[index] = float(value)    # Could fail with an invalid index
                                            # error, but we'll let python handle
                                            # it.

    def __str__(self):
        """ Returns a string representation of this VectorN (self) """
        s = "<Vector" + str(self.mDim) + ": "
        s += str(self.mData)[1:-1]
        s += ">"
        return s


    def __sub__(self, rhs):
        """ Returns the vector subtraction of self - rhs (which must be a VectorN) """
        if not isinstance(rhs, VectorN) or self.mDim != rhs.mDim:
            raise TypeError("You can only subtract another Vector" + str(self.mDim) \
                            + " to this Vector" + str(self.mDim))
        c = self.copy()
        for i in range(rhs.mDim):
            c[i] -= rhs[i]
        return c


    def __truediv__(self, divisor):
        """ Returns the result of self / divisor.  This is the same as
            s * (1 / divisor), so re-use our __mul__ operator to implement this """
        if not isinstance(divisor, int) and not isinstance(divisor, float):
            raise TypeError("You can only divide a vector by a scalar.")
        return self * (1.0 / divisor)


    def copy(self):
        """ Returns an identical (but separate) VectorN """
        return VectorN(self.mData)


    def isZero(self):
        """ Returns True if this is a zero vector, False if not. """
        for val in self.mData:
            if val != 0.0:
                return False
        return True


    def magnitude(self):
        """ Returns the scalar magnitude (length) of this vector """
        mag = 0.0
        for val in self.mData:
            valsquared = val * val
            mag += valsquared
        return mag ** 0.5


    def normalized_copy(self):
        """ Returns a normalized copy of this (non-zero) vector """
        if self.isZero():
            return ZeroDivisionError("Can't normalize a zero-vector")
        m = self.magnitude()
        new_vals = []
        for val in self.mData:
            new_vals.append(val / m)
        return VectorN(new_vals)

    def toIntTuple(self):
        """ Returns a tuple with the values of this vector, converted to integers """
        L = []
        for val in self.mData:
            L.append(int(val))
        return tuple(L)     # Converts the *list* L to a tuple and returns it

    def polar_to_cartesian(self,h,theta):
        """Will convert polar coordinates to cartesian coordinates. Must have
        h - the distance and angle theta"""
        cartesianx = h*math.cos(theta)
        cartesiany = h*math.sin(theta)
        return (cartesianx,cartesiany)

    def cartesian_to_polar(self,x,y):
        """Must have cartesian x and cartesian y"""
        r = (x**2+y**2)**0.5
        theta = math.atan(y/x)
        return (r,theta)

    def clamped(self,min_value,max_value):
        """Returns value clamped within min and max"""
        C = self.copy
        if C > max_value:
            C = max_value
        elif C < min_value:
            C = min_value

        return C


class MatrixN(object):
    def __init__(self,num_rows,num_cols):
        """ Constructor which takes number of rows and columns """
        self.rows = num_rows
        self.cols = num_cols
        if isinstance(num_rows,int) and isinstance(num_cols,int):
            self.matrix = [[VectorN((self.cols * [0.0]))] * VectorN(self.rows)]
        else:
            raise TypeError("Invalid parameter. You must pass a sequence or an integer")

    def __str__(self):
        """returns string of matrix and values """
        if MatrixN.rows>2:
            s = "/" + str(self.matrix[0]) + "\\\n"
            (s + "|" + str(self.matrix[1]) + "|\n")*self.rows-2
            s + "\\" + str(self.matrix[3]) + "/"
        else:
            s = "/" + str(self.matrix[0]) + "\\\n"
            s + "\\" + str(self.matrix[1]) + "/"

    def getRow(self,x):
        """ """
        new_row = x
        matx_row = self.matrix[0][new_row]
        return VectorN(matx_row)

    def getCol(self,y):
        """ """
        new_col = y
        matx_col = self.matrix[1][new_col]
        return VectorN(matx_col)

    def setRow(self,rowlist):
        """ """
        if not isinstance(rowlist,tuple):
            raise TypeError("Must pass a tuple of values for getCol")
        else:
            self.row_list = rowlist
            for i in range(0,self.row_list):
                setVectorRow = VectorN(i)
        return setVectorRow

    def setCol(self,collist):
        """ """
        if not isinstance(collist,tuple):
            raise TypeError("Must pass a tuple of values for getCol")
        else:
            self.col_list = collist
            for i in range(0,self.col_list):
                setVectorCol = VectorN(i)
        return setVectorCol

    def MatrixMatrixMult(self,rhs):
        """ """
        if not isinstance(rhs,MatrixN):
            raise TypeError("Must Multiply a Matrix by a Matrix")
        elif len(self.cols) != len(rhs.rows):
            raise TypeError("1st Matrix must have same amount of cols as RHS's rows")
        else:
            new_data = []
            for val in range(0,len(self.matrix)):
                for i in range(0,len(rhs[1])):
                    for j in range(0,len(rhs)):
                        new_data.append(dot(val,j))
            return MatrixN(new_data)

    def MatrixVectorMult(self,rhs):
        """ """
        if not isinstance(rhs,MatrixN):
            raise TypeError("Must Multiply a Matrix by a Matrix")
        elif len(self.cols) != len(rhs):
            raise TypeError("1st Matrix must have same amount of cols as RHS's rows")
        else:
            new_data = []
            for val in self.matrix:
                for i in range(0,len(rhs)):
                    new_data.append(dot(val,i))
            return VectorN(new_data)

    def copy(self):
        """ """
        C = self.matrix
        return C

    def transpose(self):
        """ """
        Tcopy = self.matrix.copy()
        Tmatrix = [[Tcopy.rows*[0.0]]*Tcopy.cols]
        return Tmatrix

    def identity(self,size):
        """ """
        if size >3:
            raise TypeError("Should not have a 4-5 dem identity matrix")
        else:
            self.identity_size = size
            new_matrix = copy()
            if self.identity_size == 1:
                Imatx = [[VectorN((1,0,0))]]
            elif self.identity_size == 2:
                Imatx = [[VectorN((1,0,0))],[VectorN(0,1,0)]]
            else:
                Imatx = [[VectorN((1,0,0))],[VectorN((0,1,0))],[VectorN((0,0,1))]]
        return Imatx

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@ VECTORN-related functions          @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def dot(v, w):
    """ Returns the dot product of two equally sized VectorN's """
    if not isinstance(v, VectorN) or not isinstance(w, VectorN) or \
       v.mDim != w.mDim:
        raise TypeError("You must pass two equally-sized VectorN's to the dot function")
    d = 0.0
    for i in range(v.mDim):
        d += v[i] * w[i]
    return d

def cross(v, w):
    """ Returns the cross product of two Vector3's """
    if not isinstance(v, VectorN) or not isinstance(w, VectorN) or \
       v.mDim != 3 or w.mDim != 3:
        raise TypeError("You must pass two Vector3's to the cross function")
    newX = v[1] * w[2] - v[2] * w[1]
    newY = v[2] * w[0] - v[0] * w[2]
    newZ = v[0] * w[1] - v[1] * w[0]
    return VectorN((newX, newY, newZ))

def pairwise(self,v,w):
    """Returns component wise product of v and w"""
    if not isinstance(v,VectorN) and not isinstance(w,VectorN):
        raise TypeError("V and W both must be vectorN")
    elif len(v) != len(w):
        raise TypeError("Also, V and W must be equal to one another.")
    else:
        product1 = v*w
        return VectorN((product1))


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@ (internal) TEST PROGRAMS           @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
if __name__ == "__main__":
    v = VectorN(3)
    print(v.isZero())           # True
    w = VectorN((1, -2, 3))
    print(w.isZero())           # False
    z = -w                      # Same as z = w.__neg__() to python
    print(z)                    # <Vector3: -1.0, 2.0, -3.0>
    print(z * 5)                # <Vector3: -5.0, 10.0, -15.0>   This is print(z.__mul__(5)) to python
    print(5 * z)                # <Vector3: -5.0, 10.0, -15.0>   5.__mul__(z) fails, so python calls z.__rmul__(5)
    # print(v * w)              # ERROR!
    print(z / 2)                # <Vector3: -0.5, 1.0, -1.5>     This is print(z.__truediv__(2)) to python
    #print(2 / z)                # ERROR!
    #print(z / w)                # ERROR!
    print(z.magnitude())        # 3.74165738677
    print(w.magnitude())        # 3.74165738677.   Interesting property: |-v| = |v|
    #print(z + 2)                # ERROR!
    #print(z + VectorN(2))       # ERROR!
    u = VectorN((3, 3, 3))
    print(z + u)                # <Vector3: 2.0, 5.0, 0.0>
    print(z - u)                # <Vector3: -4.0, -1.0, -6.0>
    print(z.normalized_copy())  # <Vector3: -0.2672612419124244, 0.5345224838248488, -0.8017837257372732>
    print(dot(u, z))            # -6.0
    print(cross(u, z))          # <Vector3: -15.0, 6.0, 9.0>
    #M=MatrixN(2,3)
    #print(M)