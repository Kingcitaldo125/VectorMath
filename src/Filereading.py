#Filereading

import os as operatingsys
filename = "foo.txt"
targetone = "foo"
targettwo = "Foo"
myarray = []
yescount=0
with open(filename) as file:
    content = file.readlines()
    for l in content:
        myarray.append(l)

for ll in myarray:
    if targetone in ll:
        yescount+=1
    elif targettwo in ll:
        yescount+=1

print(myarray)
#print(targettwo+" "+"Count "+str(yescount))

