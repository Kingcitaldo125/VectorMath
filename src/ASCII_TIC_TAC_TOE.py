class Names(object):
    def __init__(self):
        self.pieces = ["X","O","O","X","O","X"," "]
        self.ASCII = (self.pieces[0],"|",self.pieces[1],"|",self.pieces[2],
                    "\n-+-+-\n",self.pieces[4],"|",self.pieces[5],"|",self.pieces[6],
                    "\n-+-+-\n",self.pieces[1],"|",self.pieces[1],"|",self.pieces[1])
    def __str__(self):
        return self.ASCII

P = Names()
X = str(P)
print(X)