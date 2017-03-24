#Color Library

class ColorLibrary(object):
    def __init__(self):
        """ """
        self.colors = {"red":(255,0,0),"green":(0,255,0),
        "blue":(0,0,255),"cyan":(0,225,255),"yellow":(236,236,17),
        "orange":(234,122,7),"purple":(228,29,212),"white":(255,255,255),
        "black":(0,0,0)}

    def returncolor(self,stn):
        """ """
        red = self.colors["red"]
        blue = self.colors["blue"]
        black = self.colors["black"]
        cyan = self.colors["cyan"]
        green = self.colors["green"]
        orange = self.colors["orange"]
        purple = self.colors["purple"]
        white = self.colors["white"]
        yellow = self.colors["yellow"]

        if(stn == "blue"):
            return blue
        elif(stn == yellow):
            return yellow
        elif(stn == "black"):
            return black
        elif(stn == "red"):
            return red
        elif(stn == "purple" or stn == "violet"):
            return purple
        elif(stn == "white"):
            return white
        elif(stn == "cyan" or stn == "turquoise"):
            return cyan
        elif(stn == "green"):
            return green
        elif(stn == "orange"):
            return orange


#TEST
cl = ColorLibrary()

cyan = cl.returncolor("cyan")
red = cl.returncolor("red")
green = cl.returncolor("green")
blue = cl.returncolor("blue")
orange = cl.returncolor("orange")
purple = cl.returncolor("purple")
black = cl.returncolor("black")
yellow = cl.returncolor("yellow")
white = cl.returncolor("white")

#print(ttuple)

