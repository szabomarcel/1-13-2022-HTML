class Pont:
    def __init__(self):
        self.x = 10
        self.y = 0
    def setX(self, x):
        self.x = x 

    def getx(self):
        return self.x

pont1 = Pont()

print(pont1.getx())