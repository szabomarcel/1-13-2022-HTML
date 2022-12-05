szam1 = int(input("Írja be az első számot:"))
szam2 = int(input("Írja be a másik számot:"))
if szam1 > szam2:
    print(szam2,"kisebb mint",szam1)
elif szam1 < szam2:
    print(szam2, "nagyobb mint", szam1)
else:
    print("a két szám egyforma")