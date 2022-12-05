import random

class Szere:
    def __init__(self,nev,fog,nem,szam):
        self.nev = nev
        self.fog = fog
        self.nem = nem
        self.szam = szam

    def FvN(nem):
        if nem == "f":
            return "ferfi"
        elif nem == "n":
            return "nő"
    
t=[]
for x in range(3):
    a=input("Add meg a neved!")
    b=input("Add meg a foglalkozást!")
    c=input("Add meg a nemet! (f/n)")
    d=random.randint(1,50)
    t.append(Szere(a,b,c,d))
for x in range(3):
    print(t[x].nev,"")