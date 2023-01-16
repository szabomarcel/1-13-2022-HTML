import random

class hiresek:
    def __init__(self, neve, foglalkozasa, neme, szam):
        self.neve = neve
        self.foglalkozas = foglalkozasa
        self.neme = neme
        self.szam = szam

    def neme(neme):
        if neme == "a":
            return  "Ms"
        elif neme == "n":
            return "Frau"

t = []
for i in range(3):
    a = int(input("Add meg a nevét!"))
    b = int(input("Add meg a foglakozasat!"))
    c = int(input("Add meg a nemét!"))
    d = random.randint(1,50)
    t.append(hiresek(a, b, c, d))
for i in range(3):
    print(t[i].nev,"")