from classes import Teglalap

t1 = Teglalap()
print("A t1 kerülete: {0}, területe: {1}".format(t1.getKerulet(), t1.getTerulet()))

t1.setA(12)
t1.setB(56) 
print(f"A t1 kerülete: {t1.getKerulet()}, területe: {t1.getTerulet()}")

t1.setAB(365, 581)
print(f"A t1 kerülete: {t1.getKerulet()}, területe: {t1.getTerulet()}")

t2 = Teglalap(65, 37)
print(f"A t2 kerülete: {t2.getKerulet()}, területe: {t2.getTerulet()}")

t2.setAB(100, 200)
print(f"A t2 kerülete: {t2.getKerulet()}, területe: {t2.getTerulet()}")