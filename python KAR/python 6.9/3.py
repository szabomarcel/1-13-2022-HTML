napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

napIndex = input().lower()
napIndex = None

for i in range(0, len(napok)):
    if napIndex == napok[i].lower():
        napIndex = i
 
print(napIndex)        