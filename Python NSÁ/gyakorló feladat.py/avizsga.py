def vizsga(vizsga):
    if vizsga > 110:
        return True
    else:
        return False

nev = int(input("Add meg a vizsgázó nevét!"))
while(nev!=""):
    v = int(input("Írja be a vizsgázó pontszámtát!"))
    if vizsga(v):
        print(nev,"A vizsgája sikeres!")
    else:
        print(nev,"A vizsgája sikertelen!")
    nev = int(input("Add meg a vizsgázó nevét!"))