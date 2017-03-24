#Prints an occurance of a value * the value it's worth.
#ex: five will be printed 55555 four will be printed 4444 333 22 and so on.
numone = 5
numtwo = 5

subtracter = 5

while numone > 0:
    while numtwo > 0:
        print(str(numtwo)*subtracter)
        subtracter-=1
        numtwo-=1
    numone-=1