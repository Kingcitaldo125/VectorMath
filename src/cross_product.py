# CC1 = cross copy 1
# CC2 = cross copy 2
cc1 = [1,3,4]
cc2 = [2,-5,8]

# Cross Product #

# <y1*z2> - <z1*y2>
# <z1*x2> - <x1*z2>
# <x1*y2> - <y1*x2>

x0 = (cc1[1] * cc2[2]) - (cc1[2] * cc2[1])
x1 =(cc1[2] * cc2[0]) - (cc1[0] * cc2[2])
x2 =(cc1[0] * cc2[1]) - (cc1[1] * cc2[0])

x3 = []

x3.append(x0)
x3.append(x1)
x3.append(x2)

print(x3)