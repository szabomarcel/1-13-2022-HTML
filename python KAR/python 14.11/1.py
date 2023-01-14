def osszefesul(t1, t2):
    """A két rendezett forrás, t1 és t2 elemeit összefésüli
    a visszaadott listába. Ott is rendezve lesznek."""
    t = []
    kivonas = 0
    lista = 0
    while kivonas < len(t1) or lista < len(t2):
        if kivonas < len(t1) and (t2 >= len(t2) or t1[t1] <= t2[t2]):
            t.append(t1[t1])
            t1 += 1
        else:
            t.append(t2[t2])
            t2 += 1
    return t