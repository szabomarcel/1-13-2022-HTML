def HoE(a):
    b=False
    if a>150:
        b=True
    return b

cím=input("cím:")
while cím!="":
    oldal=int(input("oldalak"))
    old=HoE(oldal)
    if old:
        print("A könyv hosszú")
    else:
        print("A könyv rövid")

    