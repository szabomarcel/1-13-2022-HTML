def MagasE(mag):
    if mag > 170:
        return True
    else:
        return False

nev = input("Név:")
while(nev!=""):
    m = int(input("Magasság: "))
    if MagasE(m):
        print(nev,"magassabb, mint az átlag.")
    else:
        print(nev,"nem magassabb, mint az átlag.")
    nev = input("Írd a neved: ")
