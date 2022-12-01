x = int(input("Írd be a pontszámot: "))
egyek = ["elégtelen","elégséges","közepes","jó","jeles"]
doga = float(input("Pontszám"))

def érték(x):
    jegy = 1
    if doga x < 50:
        jegy = 1
    elif doga 50 <= x < 60:
        jegy = 2
    elif doga 60 <= x < 70:
        jegy = 3
    elif doga 70 <= x < 80:
        jegy = 4
    elif doga 80 <= x < 90:
        jegy = 5
    return jegy
print(jegyek[Értékes(doga)])