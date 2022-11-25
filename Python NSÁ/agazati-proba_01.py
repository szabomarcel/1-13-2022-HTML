def feladat1()
    szam1 = int(input("Írja ki az első számot: "))
    szam2 = int(input("Írja ki a második számot: "))
    if szam1 < 0 and szam2 < 0:
        print("Ez a szám negatív!")
    elif szam1 > 0 and szam2 > 0:
        print("Ez a szám pozitive!")
    elif szam1 < 0:
        print("Az első szám negatív")
    elif szam2 < 0:
        print("A második szám negatív")