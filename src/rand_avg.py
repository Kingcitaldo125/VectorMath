import random

new_list = []
for i in range(0,(random.randrange(0,20))):
    new_list.append(random.randint(0,20))
    #new_list.append(random.randint(0,20))
buffer=0
elems=0
counter=0
print("Elements: ")
for i in new_list:
    buffer+=i
    elems+=1
    #print("Elements: ")
    print(str(counter)+": "+str(i))
    #print(i)
    counter+=1

avg = buffer/elems
var = ((buffer**2)/elems) - avg**2
sd = (var)**0.5
print("Total of the list = "+str(buffer))
print("Number of elements = "+str(elems))
print("The average is: "+str(avg))
print("The variance is: "+str(var))
print("The standard deviation is: "+str(sd))
print("\n\n")