def menu():
    """ """
    mult = 20
    line000 = "Enter a selection: "
    line1 = "+"+"-"*mult+"+"
    line2 = "/"+" "*mult+"\\"
    line3 = line2
    line4 = line3
    line5 = line1
    print(line000)
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

def input_override():
    """ """
    select = input()
    if select == 1:
        pass
    elif select == 2:
        pass
    else:
        pass



myPass = "zyme9959"

attempt = input()

if(attempt == myPass):
    print("Access granted\n")
    menu();
else:
    raise TypeError("INCORRECT PASSWORD")