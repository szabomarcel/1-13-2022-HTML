import random

class hiresek:
    def __init__(self, neve, foglalkozasa, nem, szam):
        self.neve = neve
        self.foglalkozas = foglalkozasa
        self.nem = nem
        self.szam = szam

    def FgN(neme):
        if neme == "a":
            return  "Ms"
        elif neme == "n":
            return "Frau"

t = []
for x in range(3):
    a = input("Add meg a nevét!")
    b = input("Add meg a foglakozasat!")
    c = input("Add meg a nemét(a/n)!")
    d = random.randint(1,50)
    t.append(hiresek(a, b, c, d))
for x in range(3):
    print(t[x].nev,"")