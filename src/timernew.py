#Timer
import time
import os as operating

class Timer(object):
    """ """
    def __init__(self,mins,secs):
        """ """
        self.origmins = mins
        self.origsecs = secs
        self.mins = mins
        self.secs = secs
        self.countUp = False
        self.countDown = False
        self.done = False
        self.reset = 800

    def startCountUp(self):
        """ """
        self.done = False
        self.countUp = True
        self.countDown = False
        self.mins = 0
        self.secs = 0


    def startCountDown(self):
        """ """
        self.done = False
        self.countUp = False
        self.countDown = True
        self.mins = self.origmins
        self.secs = self.origsecs

        tempholder = self.reset
        tempcounter = 0
        while not self.done:
            if(self.mins <= 0):
                if(self.secs <= 0):
                    self.done = True
            tempholder-=1
            #tempcounter+=1
            if(tempholder <= 0):
                tempholder = self.reset
                self.secs-=1
                if(self.secs <= 0):
                    self.secs = 59
                    self.mins-=1
            #print(tempholder)
            #displayCurrentTime()
            #self.displayCurrentTime()
            temp = str(self.mins)
            tempp = str(self.secs)
            temppp = temp+":"+tempp
            print(temppp)


    def displayCurrentTime(self):
        """ """
        ptone = str((self.mins*100))
        ptwo = ":"
        ptthree = str((self.secs*10))
        fintemp = ptone+ptwo+ptthree
        print(fintemp)



#TESTS

#Count Down works. Count Up is not.
mins = 1
secs = 10
Tone = Timer(mins,secs)
Tone.startCountDown()
#Tone.displayCurrentTime()
