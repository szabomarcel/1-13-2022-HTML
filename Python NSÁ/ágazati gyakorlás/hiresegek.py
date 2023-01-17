import random

class hiresegek:
    def __init__(self,neve,foglalkozas,nem,szam):
        self.neve = neve
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
    a = input("Írd be a nevét!")
    b = input("Írd be a foglalkozasat!")
    c = input("Írd be a nemét!")
    d = random.randint(1,50)
    t.append(hiresegek(a, b, c, d))
for x in range(3):
    print(hiresegek.neme(t[x].nem),t[x].nev,"egy hireseg",t[x].foglakozas, t[x].szam)