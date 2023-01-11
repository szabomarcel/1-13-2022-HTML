import naptar

# print(">>>>>>Szökőév kalkulátor<<<<<<")
# ev1 = int(input("Írja be az első évet!"))
# ev2 = int(input("Írja be a második évet!"))
# szokoev = naptar.szokonapok(ev1, ev2)
# print("közötti szökőévek száma", ev1, "and" , ev2, "is: ", "ugrások", "naptar")

# ev = int(input("Adja meg a megjelenítendő évet: "))
# print(naptar.prnap(ev))

# nap = naptar.Textnaptar(naptar.SZOMBAT)
# for i in nap.időtlennapok(2017,1):
#    print(i)
# for nev in naptar.honap_nev:
#    print(nev)
# for nev in naptar.nap_nev:
#    print(nev)

#     with open("C:/Users/amirb/Desktop/naptar_module/naptar.HTML", "w") as cal:
#     c = calendar.evi_naptar.HTML(naptar.SUNDAY)
#     cal.write(c.formathonap(2020, 12))

ev = int(input('Adja meg a weboldalként megjelenítendő évet: '))
with open("file:///D:/Users/Lenovo/Documents/DszcBeregszaszi/KAR/1-13-2022-HTML/python%20KAR/python%2012.11/evi_naptar.html", "w") as cal:
    cal.write(naptar.evi_naptar.HTML(naptar.SZOMBAT).formatyear(ev))
