def bemutatkozas():
    print("A nevem majom")
    print("A korom 22")

bemutatkozas()
bemutatkozas()
bemutatkozas()
bemutatkozas()

eletkor = 21
def bemutatkozas2():
    print("Majom a nevem")
    print("eletkor")
    if eletkor > 18:
        print("Nagykorú vagyok")

def eltelt_egy_ev():
    global eletkor
    eletkor = eletkor + 1

bemutatkozas2()
eltelt_egy_ev()
bemutatkozas2()

