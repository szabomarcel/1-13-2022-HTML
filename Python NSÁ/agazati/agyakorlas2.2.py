def MagE(mag):
    if mag > 170:
        return True
    else:
        return False

nev = input("Írja be a nevét: ")
while(nev!=""):
    m = int(input("Írja be a magasságát: "))
    if MagE:
        print("Magassabb, mint az átlag!")
    else:
        print("Alacsonyabb, mint az átlag!")