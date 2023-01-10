szam1 = int(input("Adj egy számot!"))
szam2 = int(input("Adj egy másik számot!"))
if szam1 > szam2:
    print(szam1, "nagyobb, mint", szam2)
elif szam1 < szam2:
    print(szam2,"nagyobb mint",szam1)
else:
    print("A két szám egyenlő")
