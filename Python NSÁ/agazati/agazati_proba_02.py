def HoE(a):
    b=False
    if a>150:
        b=True
    return b

cim=input("cím")
while cim!="":
    oldal=int(input("oldalak"))
    old=HoE(oldal)
    if old:
        print("Az oldal túl hosszú")
    else:
        print("Az oldal túl rövid")