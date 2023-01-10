teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")

s = "Kerek a gömb, gömbszer˝u!"
teszt(cserel(s, "öm", "om") ==
"Kerek a gomb, gombszer˝u!")

teszt(cserel(s, "o", "ö") ==
"Kerek a gömb, gömbszerű!")

def cserel(s, i):
    cserel = []
    for i in range(0,len(s)):
        if s == i:
            cserel.append = s["regi"] == i["uj"]
        return True
    for x in range(0,len(s)):
        print(cserel[i].s,"")