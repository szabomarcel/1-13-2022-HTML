szam = int(input("Írj be egy egész számot: "))
if szam % 3 == 0 and szam % 5 == 0:
    print("Osztható mindkettővel")
elif szam % 5 == 0:
    print("Osztható 5-tel")
elif szam % 3 == 0:
    print("Osztható 3-mal") 
else:
    print("Nem osztható 3-mal és 5-tel")