# Tip Calculator
# Most places like people to tip %20
# Pizza guys are tipped %15
# Other miscellaneous service people like Bellhops are tipped %15

class TipC(object):
    def __init__(self,service_param,bill):
        """Either enter 'Restaurant' or 'Pizza'
        for 15-20% tip"""
        self.type = service_param
        self.total = bill

    def returnCalc(self):
        """ """
        if(self.type == "Restaurant"):
            percent = float(self.total*0.2)
            return float(percent+self.total)
        elif(self.type == "Pizza"):
            percent = float(self.total*0.15)
            return float(percent+self.total)


    def getInfo(self):
        """ """
        return self.type


svparm = "Restaurant"
bill = 60.00
tester = TipC(svparm,bill)
print(tester.returnCalc())