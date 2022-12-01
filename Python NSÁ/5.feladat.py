a = int(input("Írja be az első számot: ")) 
b = int(input("Írja be a második számot: "))
c = int(input("Írja be a harmadik számot: "))
def osszeg():
    if a + b == c:
        print("Egynelő a harmadik számmal")
    elif b + c == a:
        print("Egynelő a harmadik számmal")
    elif a + c == b:
        print("Egynelő a harmadik számmal")
