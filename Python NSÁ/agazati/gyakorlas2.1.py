szam1 = int(input("Írja be az első számot:"))
szam2 = int(input("Írja be a második számot:"))
if szam1 > szam2:
    print(szam1, "nagyobb mint", szam2)
elif szam1 < szam2:
    print(szam2, "nagyobb mint", szam1)
else:
    print("A két szám egyforma.")