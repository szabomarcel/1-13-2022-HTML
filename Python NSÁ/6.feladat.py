a = int(input("Írja be az első számot: "))
b = int(input("Írja be a második számot: "))
c = int(input("Írja be az harmadik számot: "))
if a and b and c:
    print("Osztható mindkettővel")
elif szam % 5 == 0:
    print("Osztható 5-tel")
elif szam % 3 == 0:
    print("Osztható 3-mal") 
else:
    print("Nem osztható 3-mal és 5-tel")