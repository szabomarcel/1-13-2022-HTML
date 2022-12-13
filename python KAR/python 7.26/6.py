def szavak():
    tömb = ["van", "nincs", "nem", "igen", "kincs", "ami",]
    szavak = []
    for i in tömb:
        if i != "igen":
            szavak.append(i)
        else:
            return szavak
    print(szavak)
print(szavak())