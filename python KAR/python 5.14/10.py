a = 0
b = 0
isDone = True
while isDone:
    try:
        a = int(input("Írja ki az első befogót hosszát (cm): "))
        b = int(input("Írja ki a második befogót hosszát (cm): "))
        isDone = False
    except:
        print("Rossz adatbevitel!")

print(f"A derékszögű háromszög átfogója {(((a*a) + (b*b)) ** 0.5)}cm")