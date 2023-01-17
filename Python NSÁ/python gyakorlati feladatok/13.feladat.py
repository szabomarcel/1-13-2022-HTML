osszeg = 0
a = int(input("Kerem az elso pozitiv szamot!"))
b = int(input("Kerem a masodikpozitiv szamot!"))
kulombseg = b - a + 1
for i in range(a,b + 1):
    print(i)
    osszeg = osszeg + 1
atlag = osszeg / kulombseg
atlag = round(atlag, 2)
print("A szamok osszege:",osszeg)
print("A szamok atlaga:",atlag)