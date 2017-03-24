def factoring(numb):
    """This will print out all the factors of a number entered """
    if(numb==0):
        print("ZERO DIVISION ERROR")
    else:
        count=number-1
        # Print number divided by itself

        # Print number divided by even/odd if % returns 0
        sixteen=16
        print(number/number)
        while count>=2:
            if(number%count == 0):
                print(number/count)
            count-=1
        print(number/1)

number = int(input("Enter a number"))
factoring(number)
