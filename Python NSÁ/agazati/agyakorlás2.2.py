def MagE(mag):
    if mag > 170:
        return True
    else:
        return False

nev = input("Név:")
while(nev!=""):
    m=int(input("Magasság"))
    if MagE(m):
        print("Magassabb mint az átlag.")
    else:
        print("Alacsonyabb mint az átlag.")