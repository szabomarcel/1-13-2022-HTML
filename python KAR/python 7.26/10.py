def prim_e(n):
    szam = 0 
    for i in range(1, n + 1):
        if n % 1 == 0:
            szam += 1
            if szam == 3:
                return False
    return True
