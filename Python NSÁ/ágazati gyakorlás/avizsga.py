def vizsga(v):
    if v >110:
        return True
    else:
        return False

nev = input("Írja be a vizsgázó nevét!")
while(nev!=""):
    v = int(input("Írja be a vizsgázó pontsazam!"))
    if vizsga(v):
        print(nev,"A vizsga sikeres!")
    else:
        print(nev,"A vizsga sikertelen!")
    nev = input("Írja be a vizsgázó nevét!")