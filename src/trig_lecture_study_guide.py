import math

diameter = 10 #pixels across(Random Number)
pi = 3.14159 #Circumference / Diameter
Circumference = pi * diameter

# @@@@@@@@@@@ #
# Conversions #
# @@@@@@@@@@@ #

def Conversions():
    """Degrees / Radians = 180 / pi
    All OffsetY conversions must begin/start with a negative - """
    #Polar to Cartesian:
    offsetx = distance * math.cos(theta)
    offsety = -distance * math.sin(theta)
    #Cartesian to Polar:
    distance = (offsetx**2+offsety**2) ** 0.5 #Pythagorean Theorum
    theta = math.atan2(-offsety,offsetx)

def Complimentary(number):
    """Returns the complimentary angle."""
    new_angle = 180 - number
    return new_angle

#print(Complimentary(34))
def Offset(currentx,currenty,targetx,targety):
    """Returns the offset needed to convert to polar/cartesian"""
    offsetx =  targetx - currentx
    offsety = targety - currenty
    A = offsetx
    O = offsety
    return A,O

print(Offset(50,500,200,150))

print(1-abs(math.cos(130)))