x = int(input("Írd be a pontszámot: "))
jegyek = ["elégtelen","elégséges","közepes","jó","jeles"]

def érték(x):
    jegy = 0
    if  x < 50 and x <= 0:
        jegy = 0
    elif  x >= 50 and x < 60:
        jegy = 1
    elif  x >=60 and x < 70:
        jegy = 2
    elif  x >= 70 and x < 85:
        jegy = 3
    elif  x >= 85 and x <=100: 
        jegy = 4
    return jegy

print(jegyek[érték(x)])