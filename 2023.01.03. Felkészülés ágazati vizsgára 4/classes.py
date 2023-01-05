mozgas = []
with open("fogyasztas", "r", encoding="utf-8") as autokAdat:

    print("4.feladat")
    rendszam = input("Rednszám: ")
    menetlevel = []
    for i in mozgas:
        if rendszam == i[2]:
            menetlevel.append([i[3], i[0], i[1], i[4]])

    with open(rendszam+"_mebetlevel.txt","w", encoding="UTF-8") as menLevelAdat:
        i = 0
        while i < len(menetlevel):
            menLevelAdat.write("%s\t%02d. %s\t%d 7d km"%(menetlevel[i][0], menetlevel[i][1], menetlevel[i][2], menetlevel[i][3]))
            i += 1 
            if i < len(menetlevel):
                menLevelAdat.write("\t%02d. %s\t% 7d km"%(menetlevel[i][1], menetlevel[i][2], menetlevel[i][3]))
            i += 1

print("Menetlevél kész!")