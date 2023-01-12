szam1 = int(input("Add meg az első számot! "))
szam2 = int(input("Add meg a második számot! "))
if szam1 > szam2:
    print(szam1,"nagyobb, mint", szam2)
elif szam1 < szam2:
    print(szam2,"nagyobb, mint", szam2)
else:
    print("A két szám egyforma")