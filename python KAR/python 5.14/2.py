napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasarbap"]
napI = 2

for i in range(2,137):
    if napI !=6:
        napI += 1
    else:
        napI =0

        print(f"{137 - 3} éjszakát voltál ott és {napok[napI]}i napon jössz haza.") 