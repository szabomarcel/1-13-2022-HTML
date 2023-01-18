import random

class hiresegek:
    def __init__(self,nev,foglalkozas,nem,szam):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nem = nem
        self.szam = szam
    
    def neme(neme):
        if neme == "a":
            return "Ms"
        elif neme == "n":
            return "Frau"

t = []
for x in range(3):
    a = input("Add meg a nevét!")
    b = input("Add meg a foglalkozasat!")
    c = input("Add meg a nemét!")
    d = random.randint(1,50)
    t.append(hiresegek(a, b, c, d))
for x in range(3):
    print(hiresegek.neme(t[x].neme),t[x].nev,"egy hireseg", t[x].foglalkozas, t[x].szam)