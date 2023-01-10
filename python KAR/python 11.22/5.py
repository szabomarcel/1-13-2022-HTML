teszt(vektorok_osszege([1, 1], [1, 1]) == [2, 2])
teszt(vektorok_osszege([1, 2], [1, 4]) == [2, 6])
teszt(vektorok_osszege([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

def vektorok_osszege(u, v):
    vektorok_osszege = []
    for i in range(0,len(u)):
        vektorok_osszege.append(u[i] + v[i])
    return vektorok_osszege