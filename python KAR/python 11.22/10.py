teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")

s = "Kerek a gömb, gömbszer˝u!"
teszt(cserel(s, "öm", "om") ==
"Kerek a gomb, gombszer˝u!")

teszt(cserel(s, "o", "ö") ==
"Kerek a gömb, gömbszerű!")

def cserel(s, regi, uj, nyomtatás):
    for i in range(0,len(s)):
        if s[i] == regi:
            oldstring = 'regi'
            newstring = oldstring.replace ('uj')
            nyomtatás(newstring)
            return True