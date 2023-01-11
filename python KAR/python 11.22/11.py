def csere(x, y): # Hibás változat
    print("csere utasítás előtt: x:", x, "y:", y)
    (x, y) = (y, x)
    print("csere utasítás után: x:", x, "y:", y)

a = ["Ez", "nagyon", "érdekes"]
b = [2,3,4]
print("csere függvény hívása előtt: a:", a, "b:", b)
csere(a, b)
print("csere függvény hívása után: a:", a, "b:", b)


def cserel(a, b):
    cserel = []
    for i in range(0,len(a)):
        if a == i:
            cserel.append = a["regi"] == b["uj"]
        return True
    for x in range(0,len(a)):
        print(cserel[i].a,"")

print("Hoppá!","Nem azt tette, amit szerettünk volna!")