import random

class Szere:
    def __init__(self, nev, fog, nem, szam):
        self.nev = nev
        self.fog = fog
        self.nem = nem
        self.szam = szam

    def FvN(nem):
        if nem == "f":
            return "Férfi"
        elif nem == "n":
            return "Nő"

t=[]
for x in range(3):
    a = input("Adja meg a nevét: ")
    b = input("Adje meg a foglalkozásást: ")
    c = input("Ajda meg a nemét (f/n):")
    d = random.randint(1,50)
    t.append(Szere(a,b,c,d))
for x in range(3):
    print(t[x].nev,"")