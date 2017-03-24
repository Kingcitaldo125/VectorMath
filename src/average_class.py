class average_fun(object):

    def __init__(self, num):
        """Constructor, is passed a list of numbers"""
       ## if num != []:
         ##   return str("MUST PASS A LIST OF NUMBERS.")
           ## pass
        ##elif num == ():
         ##   return str("MUST PASS A LIST OF NUMBERS, NOT A TUPLE.")
         ##   pass
        ##elif isinstance(num,str):
        ##    return str("MUST PASS A LIST OF NUMBERS, NOT A STRING")
         ##   pass
        ##else:
        self.num = num
        index = 0

        for i in self.num:
            index += i

        self.average = index / len(self.num)

    def average_calc(self):
        """Returns the average of a set of numbers"""
        index = 0

        for i in self.num:
            index += i

        self.average = index / len(self.num)
        return self.average

    def __str__(self):
        """Returns the string version of the average."""
        s1 = str("<The average of the list is: ")
        s2 = str(self.average)
        s3 = str(" percent>")
        s1 += s2
        s1 += s3
        return str(s1)

# TEST PROGRAM #

list = [100,100,75,55,43]

P = average_fun(list)

print(P)