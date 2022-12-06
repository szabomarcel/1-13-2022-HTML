def tenyezo_e(t, n):
    if  t % 2 and n % 3:
        return True
    else:
        return False




teszt(tenyezo_e(3, 12))
teszt(not tenyezo_e(5, 12))
teszt(tenyezo_e(7, 14))
teszt(not tenyezo_e(7, 15))
teszt(tenyezo_e(1, 15))
teszt(tenyezo_e(15, 15))
teszt(not tenyezo_e(25, 15)