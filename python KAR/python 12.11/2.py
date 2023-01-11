# importing copy module
import copy
 
# 1. lista inicializálása
lista1 = [1, 2, [3, 5], 4]
 
# Másolás használata sekély másolathoz
lista2 = copy.copy(lista1)
print("lista2 ID: ", id(lista2), "Value: ", lista2)

# A DeepCopy használata a DeepCopy használatához
lista3 = copy.deepcopy(lista1)
print("lista3 ID: ", id(lista3), "Value: ", lista3)