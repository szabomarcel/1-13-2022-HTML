def MagE(mag):
    if mag > 170:
        return True
    else:
        return False

nev = input("Név:")
while(nev!=""):
    m=int(input("magasság"))
    if MagE(m):
        print(nev,"magassabb, mint az átlag.")
    else:
        print(nev,"alacsonyabb, mint az átlag.")

    nev=input("Írd ki a neved:")