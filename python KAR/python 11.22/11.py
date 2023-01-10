def csere(x, y): # Hibás változat
    print("csere utasítás el˝ott: x:", x, "y:", y)
    (x, y) = (y, x)
    print("csere utasítás után: x:", x, "y:", y)

a = ["Ez", "nagyon", "érdekes"]
b = [2,3,4]
print("csere függvény hívása el˝ott: a:", a, "b:", b)
csere(a, b)
print("csere függvény hívása után: a:", a, "b:", b)

print("Hoppá!","Nem azt tette, amit szerettünk volna!")
