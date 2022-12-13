def szamok():
    tömb =[-9, -7, -5, -3, 2, -1,]
    tomeg =[]
    for i in tömb:
        if i % 2 != 0:
            tomeg.append(i)
        else:
            return tomeg
    print(tomeg)
print(szamok())

#None