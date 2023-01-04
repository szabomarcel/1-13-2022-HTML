import random

class Ember():
    def __init__(self, nev, foglalkozas, nem, szam):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nem = nem
        self.szam = szam

    def FvN(nem):
        if nem == "f":
            return "Férfi"
        elif nem == "n":
            return "Nő"

t=[]
for x in range(3):
    a = input("Add meg a nevét:")
    b = input("Add meg a foglalkozását:")
    c = input("Add meg a nemét (f/n): ")
    d = random.randint(1,50)
    t.append(Ember(a,b,c,d))
for x in range(3):
    print(t[x].nev,"")
