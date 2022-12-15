from classes import *

th1 = Teglalaphasab()
print("A th1 felszíne: {0}, térfogata: {1}".format(th1.getFelszíne(), th1.getTérfogata()))

th1.setA(12)
th1.setB(14)
th1.setC(16)
print(f"A th1 felszíne: {th1.Felszíne()}, térfogata: {th1.getTérfogata()}")

th2 = Negyzet(65)
print(f"A th2 felszíne: {th2.getFelszíne()}, térfogata: {th2.getTérfogata()}")

th2.setABC(100, 200, 300)
print(f"A th2 felszíne: {th2.getFelszíne()}, térfogata: {th2.getTérfogata()}")