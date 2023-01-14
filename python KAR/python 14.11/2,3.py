teszt(ugyanazon_az_atlon(5,2,2,0) == False)
teszt(ugyanazon_az_atlon(5,2,3,0) == True)
teszt(ugyanazon_az_atlon(5,2,4,3) == True)
teszt(ugyanazon_az_atlon(5,2,4,1) == True)

# Olyan megoldási esetek, amikor nincsenek ütközések
teszt(oszlop_utkozes([6,4,2,0,5], 4) == False)
teszt(oszlop_utkozes([6,4,2,0,5,7,1,3], 7) == False)

# További tesztesetek, amikor többnyire ütközések vannak
teszt(oszlop_utkozes([0,1], 1) == True)
teszt(oszlop_utkozes([5,6], 1) == True)
teszt(oszlop_utkozes([6,5], 1) == True)
teszt(oszlop_utkozes([0,6,4,3], 3) == True)
teszt(oszlop_utkozes([5,0,7], 2) == True)
teszt(oszlop_utkozes([2,0,1,3], 1) == False)
teszt(oszlop_utkozes([2,0,1,3], 2) == True)



def ugyanazon_az_atlon(x0, y0, x1, y1):
    dy = abs(y1 - y0) # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0) # Kiszámoljuk x távolságának abszolút értékét
    return dx == dy # Ütköznek, ha dx == dy

def oszlop_utkozes(bs, c):
    for i in range(c): # Nézd meg az összes oszlop
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True
            return False # Nincs ütközés, a c oszlopban biztonságos helyen
