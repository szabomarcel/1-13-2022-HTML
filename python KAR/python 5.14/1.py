napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasarbap"]

try:
    napIndex = int(input("Írjak be a napok számát (1-7)"))
    print(napok[napIndex - 1])
except:
    print("Nem helyes formátum!")