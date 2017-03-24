import math
import __main__

class Averager(object):
    def __init__(self,lists):
        """ """
        self.counter = 0
        self.num = 0
        self.list = lists
        main_list = []

    def avg(self):
        """ """
        self.zed = 0
        main_list.append(self.list)
        for i in self.list:
            self.zed+=i

        #return self.counter,self.num

    def __str__(self):
        """ """
        Averager.avg(self)
        str_ctr = str(self.counter)
        str_num = str(self.num)
        return self.counter,self.num

main_list = [10,35,35,40,40,35,30]
zed = 0
A = Averager(main_list)
print(A)
