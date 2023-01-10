f = open("szoveg.txt")
tartalom = f.read()
f.close()

f.sort()

g = open("rendezett.txt", "w")
for v in f:
    g.write(v)
g.close()