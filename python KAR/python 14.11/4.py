import random

def van_utkozes(sakktabla):
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
            return False

def main():    
    rng = random.Random() # A generátor létrehozása
    bd = list(range(8)) # Generálja a kezdeti permutációt
    talalat_szama = 0
    proba = 0
    while talalat_szama < 10:
        rng.shuffle(bd)
        proba += 1
    if not van_utkozes(bd):
        print("Megoldás: {0}, próbálkozás: {1}.".format(bd, proba))
    proba = 0
    talalat_szama += 1