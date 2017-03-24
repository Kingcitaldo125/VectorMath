class Player(object):
    def __init__(self, newname):
        self.name = newname
    def __str__(self):
        return str("Hi, I'm ") + self.name

P1 = Player("Bob")
x = str(P1)
print(x)
