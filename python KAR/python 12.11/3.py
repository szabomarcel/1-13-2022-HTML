import copy 

regi_lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

uj_lista = copy.deepcopy(regi_lista)

uj_lista[0][2] = "c"

print("Régi lista", regi_lista)
print("Új lista", uj_lista)