teszt(skalaris_szorzat([1, 1], [1, 1]) == 2)
teszt(skalaris_szorzat([1, 2], [1, 4]) == 9)
teszt(skalaris_szorzat([1, 2, 1], [1, 4, 3]) == 12)

def skalaris_szorzat(u, v):
    szorzat = []
    for i in range(0,len(u)):
        szorzat.append(u[i] * v[i])
    return szorzat