def fib(nn):
    xx, yy, Fn = 0, 1, 1
    for ii in range(1,nn):
        Fn = xx + yy
        xx = yy
        yy = Fn

    return Fn

fib_range = 250
for i in range (0,fib_range):
    L = fib(i)
    print(L)


#L = fib(250)
#print(L)
