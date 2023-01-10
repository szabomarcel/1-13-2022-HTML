f = open("szoveg.txt")
tartalom = f.read()
f.close()

szavak = tartalom.split()
print("A fájl szavainak száma: {0}.".format(len(szavak)))