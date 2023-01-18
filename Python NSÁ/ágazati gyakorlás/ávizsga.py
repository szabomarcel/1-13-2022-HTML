def vizsga(vizsga):
    if vizsga > 110:
        return True
    else:
        return False

nev = input("Írd be a vizsgázó nevét!")
while(nev!=""):
    v = int(input("Írd be a vizsgázó pontszámát!"))
    if vizsga(v):
        print("A vizsga sikeres!")
    else:
        print("A vizsga sikertelen!")
    nev = input("Írd be a vizsgázó nevét!")

