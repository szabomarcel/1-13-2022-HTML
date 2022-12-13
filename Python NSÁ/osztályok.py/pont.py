class Pont:
    def __init__(self):
        self.x = 10
        self.y = 0
    def setX(self, x):
        self.x = x 

    def getx(self):
        return self.x

pont1 = Pont()
pont2 = Pont()

pont2.setX(100)
print(pont1.getx())
print(pont2.getx())