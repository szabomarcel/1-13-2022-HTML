

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2,]
jegyek = ["elégtelen","elégséges","közepes","jó","jeles"]
doga = float(input("Pontszám"))

def Értékes(pont):
    jegy = 0
    if doga <60 and doga >=0:
        jegy = 0
    elif doga >= 60 and doga <70:
        jegy = 1 
    elif doga >= 70 and doga <80:
        jegy = 2
    elif doga >= 80 and doga <90:
        jegy = 3
    elif doga >=90 and dog <100:
        jegy = 4
    return jegy
print(jegyek[Értékes(doga)])

