import random

class hiresek():
    def __init__(self, neve, foglalkozas, neme, szam):
        self.nev = neve
        self.foglalkozas = foglalkozas
        self.neme = neme
        self.szam = szam

    def neme(neme):
        if neme == "a":
            return "Ms"
        elif neme == "n":
            return "Frau"

t = []
for i in range(3):
    a = int(input("Adja meg a nevét!"))
    b = int(input("Adja meg a foglalkozását!"))
    c = int(input("Adja meg a nemét!"))
    d = random.randint(1,50)
    t.append(hiresek(a, b, c, d))
for i in range(3):
    print(t[i].nev,"")