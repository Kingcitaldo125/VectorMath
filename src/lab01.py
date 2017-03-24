#Paul Arelt
#lab 01
#ETGG 1801 01

fName = str("Paul")
lName = str("Arelt")
print(fName,lName);
print(fName,lName,sep=";");
num1 = 18.4
num_form = num1**(1/3)
print("The cube root of "+ str(num1) + " is " + str(num_form))

hours = 13
mins = 53
secs = ((hours*60)*60) + (mins*60)
print("THere are " + str(secs) + " seconds in " + str(hours) + " hours and " + str(mins) + " mins.\n");

diameter = 16
cost = 15
cost_per_square = (cost/diameter)
print("The cost per square inch of a " + str(diameter) + "-inch diameter $" + str(cost) + " pizza is $" + str(cost_per_square));

print("Press enter to quit....");
enter = input("Press enter to quit")
raise SystemExit

