import sys

def teszt(sikeres_teszt):
    """ Egy teszt eredményének mejelenítése"""
    sorszam = sys._getframe(1).f_lineno# A hívó sorának száma
    if sikeres_teszt:
        msg = " A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN".format(sorszam))
    print(msg)

teszt(3 % 4 == 0)
teszt(3 % 4 == 3)
teszt(3 / 4 == 0)
teszt(3 // 4 == 0)
teszt(3+4 * 2 == 14)
teszt(4-2+2 == 0)
teszt(len("helló, világ!") == 13)