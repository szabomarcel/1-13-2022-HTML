a = 0
b = 0
c = 0

isDone = True
while isDone:
    try:
        a = int(input("Írja ki az első befogót hosszát (cm): "))
        b = int(input("Írja ki a második befogót hosszát (cm): "))
        c = int(input("Írja ki a harmadik befogót hosszát (cm): "))
        isDone = False
    except:
        print("Rossz adatbevitel!")

if abs()