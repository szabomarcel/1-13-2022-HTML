class Teglalap:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
        
    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b
        
    def setAB(self, a, b):
        self.a = a
        self.b = b
        
    def getA(self):
        return self.a
    
    def getKerulet(self):
        return 2 * (self.a + self.b)
    
    def getTerulet(self):
        return self.a * self.b
    

class Negyzet:
    def __init__(self, a = 0):
         self.a = a
        
    def setA(self, a):
        self.a = a
    
    def getA(self):
        return self.a
    
    def getKerulet(self):
        return 4 * self.a
    
    def getTerulet(self):
        return Negyzet.pow(self.a, 2)
    
    
class Kor:
    
    def __init__(self, r):
        self.r = r
        
    def setR(self, r):
        return self.r
    
    def getKerulet():
        return 2 * r * 3.14
    
    def getTerulet():
        return 2 * r * 3.14

class Teglalaphasab:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getFelszin(self, a, b, c):
        return a * b * c
    def getTerfogat(self, a, b, c):
        return 2 * (a * b) + (b * c) + (c * a)

class ember:
    def __init__(self, neve, neme, koszon):
        self.neve = neve
        self.neme = neme
        self.koszon = koszon

print("Jó ember")
a = ember((input("Neve:")), int(input("Neme:")), int(input("Köszön:")))
print(a.neve)
print(a.neme)
print(a.koszon)