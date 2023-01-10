def vizsga(vizsga):
    if vizsga > 110:
        return True
    else:
        return False
    
név = input("Add meg a vizsgázó nevét!")
while (név!=""):
    v = int(input("Add meg a pontszámot!"))
    if vizsga(v):
        print("A vizsgája sikeres!")
    else:
        print("A vizsgálya sikertelen!")
    nev = input("Add meg a vizsgázó nevét")