# függvények példa

import random # külső csomagok importálása


# függvényekdef gép_válasza(e):
    return random.choice(e[0:3])

def döntés(a, b):
    if a == b:
        print("Döntetlen")
    elif a == "flex":
        print("Oké, oké... neyrtél!")
    elif (a == "kő" and b == "papír") or \
            (a == "papír" and b == "olló") or \
            (a == "olló" and b == "kő"):
        print("Vesztettél!")
    else:
        print("Nyertél!")

def játék(e):
    j ="" # játékos válasza
    while j not in e:
        j = input(f"Mit választasz? {e[0:3]}")
    g = gép_válasza(e)
    print(f"A gép válasza: {g}")
    döntés(j, g)



eszközök =["kő", "papír", "olló", "flex"]
while True:
    játék(eszközök)