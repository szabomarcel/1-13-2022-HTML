def vizsga(vizsga):
    if vizsga > 110:
        return True
    else:
        return False

nev = input("Írbe be a vizsgázó nevét!")
while(nev!=""):
    v = int(input("Írd be a vizsgázó pontszámét!"))
    if vizsga(v):
        print("A vizsga sikeres!")
    else:
        print("A vizsga sikertelen!")
    nev = input("Írbe be a vizsgázó nevét!")