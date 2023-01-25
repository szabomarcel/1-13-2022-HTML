import random

class hiresegek:
    def __init__(self,neve,foglalkozas,nem):
        self.neve = neve
        self.foglalkozas = foglalkozas
        self.nem = nem

    def neme(neme):
        if neme == "a":
            return "Ms"
        elif neme == "n":
            return "Frau"

t = []
for x in range(3):
    a = input("Add meg a vizsgázó nevét!")
    b = input("Add meg a vizsgázó foglalkozását!")
    c = input("Add meg a vizsgázó nemét!")
    d = random.randint(1,50)
    t.append(hiresegek(a, b, c, d))
for x in range(3):
    print(hiresegek.neme(t[x].neme),t[x].nev,"egy hireseg", t[x].foglalkozas)