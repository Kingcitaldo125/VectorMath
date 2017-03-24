#Thermometer gague for home

import time
clock = time.clock()

coolsettings = {}
heatsettings = {}
maxdict = {}
mindict = {}

class Thermometer(object):
    def __init__(self,start,maxn,minn):
        """ """
        self.temp = start
        self.maxtemp = maxn
        self.mintemp = minn
        self.checkTimer = 0.0
        self.localTimer = 0.0
        self.running = False

    def runTimer(self):
        """ """
        if self.running:
            self.localTimer+=clock

    def startTimeIteration(self):
        """ """
        if self.running:
            localTimer+=clock
        else:
            self.running = True

    def endTimeIteration(self):
        """ """
        if self.running:
            self.running = False
        else:
            print("Time Error")

    def runCool(self):
        """Run the AC """

    def runHeat(self):
        """Run the Heat """

    def returnCurrTemp(self):
        """ """
        return self.temp

    def checkHeat(self):
        """Check to see if the house is too warm """
        if self.temp >= maxtemp:
            self.runCool()

    def checkCool(self):
        """Check to see if the house is too cold """
        if self.temp <= self.mintemp:
            self.runHeat()

    def reset(self):
        """ """
        self.checkTimer = 0.0
        self.localTimer = 0.0
        self.running = False

#Base Test
therm = Thermometer(60,72,32)
done=False