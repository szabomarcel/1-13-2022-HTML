import random

class Szere():
    def __init__(self, neve, foglalkozas, nem, szam):
        self.neve = neve
        self.foglalkozas = foglalkozas
        self.nem = nem
        self.szam = szam
    
    def nem(nem):
        if nem == "f":
            return "Férfi"
        elif nem == "n":
            return "Nő"

t = []
for x in range(3):
    a = input("Add meg a nevét: ")
    b = input("Add meg a foglalkozását: ")
    c = input("Add meg a nemét: ")
    d = random.randint(1,50)
    t.append(Szere(a,b,c,d))
for x in range(3):
    print(t[x].nev,"")