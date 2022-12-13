def feladat1():
    szam1 = int(input("Adjon meg az első számot: "))
    szam2 = int(input("Adjon meg a második számot: "))
    if szam1 < 0 and szam2 < 0:
        print("A szám negatív")
    if szam1 > 0 and szam2 > 0:
        print("A szám pozitív")
    if szam1 < 0:
        print("Az első szám negatív")
    if szam2 < 0:
        print("A második szám negatív")