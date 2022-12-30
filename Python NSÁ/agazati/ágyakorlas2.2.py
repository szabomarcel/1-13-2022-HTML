def MagE(mag):
    if mag > 170:
        return True
    else:
        return False

nev = input("Név: ")
while(nev!=""):
    m = int(input("Írja be a nevét: "))
    if MagE(m):
        print("Az átlagnál magassabb!")
    else:
        print("Az átlagnál alacsonybb!")
    nev = input("Írd meg a neved:")