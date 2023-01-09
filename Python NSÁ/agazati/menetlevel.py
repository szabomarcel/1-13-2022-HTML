from classes import Menetlevél

r = open("fogyasztas.txt", "r")
jarmuvek = []

for line in r:
    jarmu_adatok = line.split(";")
    jarmu = Menetlevél()
    jarmu.setMegtettkm(int(jarmu_adatok))
    jarmu.setÖsszÜzemanyag(float(jarmu_adatok[2][0:len(jarmu_adatok[2])-2]))    
    jarmuvek.append(jarmu)
r.close

r = open("atlagfogyasztas.txt")
for jarmu in jarmuvek:
    r.write(f"{jarmu.getrendszam},{jarmu.atlagfogyasztas}")
    print(f"{jarmu.getrendszam},{jarmu.atlagfogyasztas}")
r.close