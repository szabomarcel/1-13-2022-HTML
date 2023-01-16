def vizsga(v):
    if v > 110:
        return True
    else:
        return False

nev = int(input("Írja be a vizsgázó nevét!"))
while(nev!=""):
    v = int(input("Írja be a vizsgázó pontszámot!"))
    if vizsga(v):
        print("A vizsga sikeres!")
    else:
        print("A vizsga sikerteken!")
    nev = input("Írja ne a vizsgázó nevét!")