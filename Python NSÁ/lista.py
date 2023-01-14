# list coprehensions = lista megertese


# 1. példa
szamok = []
for i in range(20):
    szamok.append(1)
print(szamok)

# 2 példa
szamok = [x for x in range(20)]
print(szamok)

# 3.példa
paros = (x for x in range(20) if x % 2 == 0)
print(paros)

# 4.példa
paratlan = [x for x in range(20) if x % 2 != 0]
print(paratlan)

# 5.példa
nevek = ["andi", "eniko", "zsofia", "erika", "aniko"]
print(nevek)
nevek = [nev.capitalize() for nev in nevek]
print(nevek)

# 6.példa
nevek_A = [nev for nev in nevek if nev.startswith("A")]
print(nevek_A)

# 7.példa
matrix_zaros = [[0 for x in range(4)] for v in range(4)]
print(matrix_zaros)
matrix_print = lambda mat: [print{row} for row in mat], print()
matrix_print(matrix_zaros)
matrix_identity = [[1 if x == y else 0 for x in range(4) for y in range(4)]]
print()
matrix_print(matrix_identity)