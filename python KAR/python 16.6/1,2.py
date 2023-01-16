class Teglalap:
    def __init__(self, terulet, kerulet):
        self.terulet = terulet
        self.kerulet = kerulet

    def kijelzo(self):
        print("Kérema a téglalap alapját:", self.a)
        print("Kérema a téglalap magasságát:", self.b)
    
    def terulet(self):
        return(self.a * self.b)
    
    def kerulet(self):
        return(2 * self.terulet + 2 * self.kerulet)


a = int(input("Kérem a téglalap alapját:"))
b = int(input("Kérem a télalap magasságát:"))

r1 = Teglalap(a, b)
print("A téglalap eltakarja a részleteket: ")
r1.kijelzo()
print("")
print("A téglalap területe", r1.terulet)
print("")
print("A téglalap kerülete", r1.kerulet)








p = Pont(4, 2)
s = Pont(4, 2)
print("Az == eredménye Pontokra alkalmazva:", p == s)
# Alapértelmezés szerint az == a Pont objektumoknál
# referencia szerinti egyenloséget néz. ˝

a = [2,3]
b = [2,3]
print("Az == eredménye listákra alkalmazva:", a == b)
# A listáknál viszont az érték szerinti egyenloségvizsgálat ˝
# az alapértelmezett.
