#for i in range(1, 6,2): # prints 1, 3, then 5
 #   print(i)

s = [[0,1,2], [3,4,5], [6,7,8]]

def First():
    """Will print the first object in each sublist, no matter the length of the
    sublist"""
    for i in s:
        print(i[0])

First()