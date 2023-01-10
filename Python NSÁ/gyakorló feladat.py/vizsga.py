def vizsga(vizsga):
    if vizsga > 110:
        return True
    else:
        return False

név = input("Írja be a nevét! ")
while(nev!=""):
    v = int(input("Írja be a pontszámát! "))
    if vizsga(v):
        print("A vizsgája sikeres!")
    else:
        print("A vizsgája sikertelen!")
    nev = input("Írja be a nevét!")