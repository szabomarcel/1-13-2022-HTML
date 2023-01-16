file = open("mondasok.txt", "r", encoding="utf-8")

for sor in file:
    print(sor.strip())

sor = file.readline()
while sor:
    print(sor)
    sor = file.readline()

file.close()

with open("mondasok.txt", "r", encoding="utf-8") as file:
    for sor in file:
        print(sor.strip())

with open("mondasok.txt", "r", encoding="utf-8") as file:
    sor = file.readline()
    while sor: 
        print(sor.strip())
        sor = file.readline