import random

class hiresegek:
    def __init__(self, neve, foglalkozas, neme, szam):
        self.neve = neve
        self.foglalkozas = foglalkozas
        self.neme = neme
        self.szam = szam

    def neme(neme):
        if neme == "a":
            return "Ms"
        elif neme == "n":
            return "Frau"

t = []
for x in range(3):
    a = input("Add meg a nevét!")
    b = input("Add meg a foglalkozását!")
    c = input("Add meg a nemét!")
    d = random.randint(1,50)
    t.append(hiresegek(a, b, c, d))
for i in range(3):
    print(t(x).nev,"")