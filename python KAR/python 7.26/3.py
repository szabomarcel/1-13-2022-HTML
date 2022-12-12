def osszegzes():
    tömb = [-9,-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = -1
    for i in tömb: 
        if i % 2 == 0:
            a = a +- 1
    print(a)
print(osszegzes())