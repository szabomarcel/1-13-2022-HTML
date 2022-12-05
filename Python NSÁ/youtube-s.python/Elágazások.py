eletkor = 10
if eletkor > 18:
    print(" Te már nem vagy gyerek!")
    print("Mert idősebb vagy mind 18.")
print("Vége")

if eletkor < 18:
    print("Gyerek vagy.")

if eletkor == 18:
    print("Most lettél felnőtt.")

nev = "István"
if eletkor < 18 and nev == "István":
    print("Pityuka")

nev = "Marcell"
if nev == "Marcell":
    nev = nev + "ka"
print(nev)

irany = input("Merre mennél? ")
print("Meghaltál, mert arra volt a sárkány")