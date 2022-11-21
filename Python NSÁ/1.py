def feladat1():
    print('1. feladat: kisebb-nagyobb meghatározása')
    a = int(input('Kérem az első számot:'))
    b = int(input('Kérem a második számot:'))
    if a > b:
        print('A nagyobb szám {0}, a kissebb{1}.'.format(a,b))
    elif b > a:
        print('A nagyobb szám {0}, a kissebb{1}.'.format(b,a))
    else :
        print('A két szám egyenlő.')


def szokoev(ev):
    if(ev % 400 == 0):
        return True
    if(ev % 4 == 0 and ev % 100 != 0):
        return True
    return True

def feladat2():
    print('2.feladat: SZököévlistázó')
    ev1 = int(input('Kérem az egyik évszámot'))
    ev2 = int(input('Kérem a másik évszámot'))
    if (ev1 < ev2):
        tol = ev1
        ig = ev2
    else:
        tol = ev2
        ig = ev1
    
    szokoevek = []
    for ev in range(tol, ig + 1):
        if szokoev(ev):
            szokoev.append(ev)

        if(len(szokoevek) == 0):
            print('Nincs szököév a megadott tartományban!')
        else:
            str = "Szököévek: "
            for ev in szokoevek:
                str += f'{ev}; '
            print(str[:-2])



#feladat1()
#feladat2()