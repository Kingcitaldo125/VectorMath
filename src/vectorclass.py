#vector constructor
#addition
class TempVector2D(object):
    def __init__(self,x,y):
        """ """
        self.holder = []
        self.size = 2.0
        self.sizeint = 2
        self.x = float(x)
        self.y = float(y)
        self.holder.append(x)
        self.holder.append(y)

    def __len__(self):
        """ Returns the dimension of this VectorN when a VectorN is passed to
           the len function (which is built into python) """
        return self.size

    def __str__(self):
        """ Returns a string representation of this VectorN (self) """
        s = "<Vector" + str(self.sizeint) + ": "
        s += str(self.holder)[1:-1]
        s += ">"
        return s

    def __getitem__(self,index):
        """ """
        idx = self.holder[index]
        return idx

    def __setitem__(self,index,value):
        """ """
        if not isinstance(value,float):
            raise TypeError("Must pass a floating point value")
        self.holder[index] = float(value)

    def copy(self):
        """ """
        return TempVector2D(self.x,self.y)

    def __add__(self,other):
        """Adds two vectors,returns list in vector form"""
        if not isinstance(other,TempVector2D):
            raise TypeError("must have two TempVector2D's")
        if not isinstance(other.x,float):
            raise TypeError("must have two floating points")
        if not isinstance(other.y,float):
            raise TypeError("must have two floating points")

        if(other.size != self.size):
            raise TypeError("Must pass a 2D vector.")
        current = self.copy()
        for i in range(self.sizeint):
            current[i]+=other[i]
        return current

    def __sub__(self,other):
        """Subtracts two vectors,returns list in vector form"""
        if not isinstance(other,TempVector2D):
            raise TypeError("must have two TempVector2D's")
        if not isinstance(other.x,float):
            raise TypeError("must have two floating points")
        if not isinstance(other.y,float):
            raise TypeError("must have two floating points")

        current = self.copy()
        for i in range(self.sizeint):
            current[i]-=other[i]
        return current

    def returnCurrentValuePair(self):
        """Will return a list of two vector values."""
        tempholder = []
        tempholder.append(self.x)
        tempholder.append(self.y)
        return tempholder

# used for testing

tempx = 200
tempy = 100

#Create a new vector
newvector = TempVector2D(tempx,tempy)

assert(newvector.x == tempx)
assert(newvector.y == tempy)

#See the values
print(newvector)

#Add some value
other = TempVector2D(100,100)
print("Other")
print(other)
print("Sum")
print(newvector+other)
print("Difference")
print(newvector-other)

