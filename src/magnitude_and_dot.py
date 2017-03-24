def dot(x,y):
    """Returns the dot product of vector"""
    addedindex1 = 0
    addedindex2 = 0
    for i in x:
        addedindex1 += i
    for i in y:
        addedindex2 += i

    return addedindex1/addedindex2

vector1 = [5,4,7]
vector2 = [1,7,6]

index = 0
indexlist = []
for i in vector1:
    i**=2
    index += i
indexlist.append(index)

indexlist[0]**=0.5

zed1 = vector1
zed2 = indexlist
z = dot(zed1,zed2)
print("The magnitude of", str(zed1),"is: ",indexlist)
print("The dot product is: ", z, "(sum of",zed1,"/",zed2,")")