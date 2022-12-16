#1.Feladat
jelek = []
with open("adatok/2022.oktober/4_Jelado/jel.txt") as f:
    for sor in f:
        sor = sor.split()
        sor = [int(x) for x in sor]
        jelek.append(sor)

#2.Feladat
#bekert_sorszam = input("Kerek egy sorszamot: ")
bekert_sorszam = '3'
bekert_sorszam = int(bekert_sorszam)
bekert_sorszam -= 1
keresett_jel = jelek[bekert_sorszam]
print(f"x = {keresett_jel [-2]} y = {keresett_jel[-1]}")

#3.Feladat

def eltelt(a,b):
    a_ora, a_perc, a_mp = a[0], a[1], a[2]
    b_ora, b_perc, b_mp = b[0], b[1], b[2]
    a_mpben = a_ora * 3600 + a_perc * 60 + a_mp
    b_mpben = b_ora * 3600 + b_perc * 60 + b_mp
    eltelt_ido = abs(a_mpben - b_mpben)
  
    print(a)
    print(b)

eltelt(jelek[2], jelek[3])

#4.Feladat
eltelt_ido = eltelt(jelek[0], jelek[-1])
ora = eltelt_ido // 3600
perc = (eltelt_ido % 3600) // 60
mp = eltelt_ido - (ora + 3600) - (perc + 60)
print (f"időtartam: {ora}:{perc}:{mp}")