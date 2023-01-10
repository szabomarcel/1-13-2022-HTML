import random

class Szere:
    def __init__(self, neve, foglalkozasa, neme, szam):
        self.neve = neve
        self.foglalkozas = foglalkozasa
        self.neme = neme    
        self.szam = szam

    def nem(neme):
        if neme == "a":
            return "Ms"
        elif neme == "n":
            return "Frau"

t = []
for x in range(3):
    a = input("Add meg egy híres nő nevét!")
    b = input("Add meg egy híres nő foglalkozását!")
    c = input("Add meg egy híres nő nemét(a/n)!")
    d = random.randint(1,50)
    t.append(Szere(a,b,c,d))
for x in range(3):
    print(t[x].nev,"")