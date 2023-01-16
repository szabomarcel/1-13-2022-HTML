import teszt

class Teglalap():
    def __init__(self, tartalmazza_e, pont):
        self.tartalmazza_e = tartalmazza_e
        self.pont = pont

    

r = Teglalap(Pont(0, 0), 10, 5)
teszt(r.tartalmazza_e(Pont(0, 0)))
teszt(r.tartalmazza_e(Pont(3, 3)))
teszt(not r.tartalmazza_e(Pont(3, 7)))
teszt(not r.tartalmazza_e(Pont(3, 5)))
teszt(r.tartalmazza_e(Pont(3, 4.99999)))
teszt(not r.tartalmazza_e(Pont(-3, -3)))


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



