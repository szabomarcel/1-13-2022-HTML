import random

class Szere:
    def __init__(self, nev, foglalkozas, nem, szam):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nem = nev
        self.szam = nev

    def nem(nem):
        if nem == "f":
            return "Férfi"
        elif nem == "n":
            return "Nő"

t = []
for x in range(3):
    a = input("Add meg a neved: ")
    b = input("Add meg a foglalkozásod: ")
    c = input("ADd meg a nemed: ")
    d = random.randint(1,50)
    t.append(Szere(a,b,c,d))
for x in range(3):
    print(t[x].nev,"")