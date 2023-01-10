def feladat1():
    szam1 = int(input("Adj meg egy számot: "))
    szam2 = int(input("Adj meg másik számot: "))
    if szam1 < 0 and szam2 < 0:
        print("Mindkét szám negatív")
    elif szam1 > 0 and szam2 > 0:
        print("Mindkét szám pozitív")
    elif szam1<0:
        print("Az első szám negatív")
    elif szam2<0:
        print("A második szám negatív")