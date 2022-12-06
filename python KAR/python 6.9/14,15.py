def paratlan_e(n):
    if n % 2:
        return True
    else:
        return False

n = int(input("Adj meg egy számot:"))
print(paros_e(n))


print(paros_e(2))
print(paros_e(0))
print(paros_e(1))
print(paratlan_e(2))
print(paratlan_e(0))
print(paratlan_e(1))