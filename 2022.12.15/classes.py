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
        return math.pow(self.a, 2)
    
    
class Kor:
    
    def __init__(self, r):
        self.r = r
        
    def setR(self, r):
        return self.r
    
    def getKerulet():
        return 2 * r * 3.14
    
    def getTerulet():
        return 2 * (r) * 3.14
    