import evek

a = int(input("Írd be az elöző születésnapod!"))
b = int(input("Írd be az elöző születésnapod!"))
if a > b:
    print(a,"nagyobb mint az elöző év!",b)
elif a < b:
    print(b,"nagyobb mint az elöző év!",a)

def ev(ev):
    if ev >= "ev":
        return True
    elif ev <= "ev":
        return False

t = []
for x in range(3):
    print(t(x).ev,"")