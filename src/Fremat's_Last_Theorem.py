import math

#Fremat's Last Theorom

class Theory1(object):
    def __init__(self,x,y,z):
        """ """
        self.X = x;
        self.Y = y;
        self.Z = z;

    def __str__(self):
        """ """
        num1 = self.X**2;
        num2 = self.Y**2;
        num3 = self.Z**2;
        res1 = num1+num2
        return_state = "The result is: X= " + str(num1) + " Y= " + str(num2) + " Z= " + str(num3)
        return return_state;

num1 = 3
num2 = 4
num3 = 5
T = Theory1(num1,num2,num3);
print("Fremat's Last Theorem");
print("You have entered " + str(num1) +" "+ str(num2) +" "+ str(num3)+" as your number choices..");

print(T)

