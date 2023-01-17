def vizsga(vizsga):
    if vizsga > 110:
        return True
    else:
        return False

név = input("Írja be a nevét!")
while(név!=""):
    v = int(input("Írja be a pontszámot!"))
    if vizsga(v):
        print(név,"A vizsga sikeres!")
    else:
        print(név,"A vizsga sikertelen!")
    név = (input("Írja be a nevét!"))