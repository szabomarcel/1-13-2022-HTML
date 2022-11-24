a = 0
b = 0

isDone = True
while isDone:
    try:
        a = int(input("Írja be az első befogadót osszát (cm)"))
        a = int(input("Írja be az második befogadót osszát (cm)"))
        isDone = False
    except:
        print("Rossz adatbevitel!")

print(f"A derékszögű háromszög átfogója {(((a*a) + (b*b)) ** 0.5)}cm.")