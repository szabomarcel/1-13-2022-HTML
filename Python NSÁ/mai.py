import random

#Tömbös progi
#t=[1,3,5,7,"jolán"]
#print(t)
t=[]
for i in range(5):
    t.append(random.randint(1,100))
print(t)

#Összegzés tétel
osszeg=0
for x in t:
    osszeg+=x
print(osszeg)

#Átlagtétel
atl=osszeg/len(t)
print(atl)

#Min
min=101
for i in t:
    if min>x:
        min=x
print(min)

#Max
min=-1
for i in t:
    if max<x:
        max=x
print(max)