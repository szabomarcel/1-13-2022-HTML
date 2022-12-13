def long(a):
    b = False
    if b > 150:
        b = True
    return b
    
cím = input("Írja be a könyv címét: ")
while cím!="":
    oldal = int(input("oldalak"))
    old = long(oldal) 
    if oldal:
        print("A könyv túl hosszú!")
    else:
        print("A könyv túl rövid!")