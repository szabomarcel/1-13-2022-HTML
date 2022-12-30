def MagE(mag):
    if mag > 170:
        return True
    else:
        return False

név = input("Írja be a nevét: ")
while(nev!=""):
    m = int(input("Írja be a magasságát: "))
    if MagE(m):
        print("Az átlagnál magassabb: ")
    else:
        print("Az átlagnál alacsonyabb: ")
    nev = input("Írja be a nevét: ")