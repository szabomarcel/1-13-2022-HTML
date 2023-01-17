a = int(input("Add meg az első számot!"))
b = int(input("Add meg a második számot!"))
if a > b:
    print(a,"nagyobb, mint",b)
elif a < b:
    print(b, "nagyobb, mint",a)
else:
    print("A két szám egyforma!")