from classes import *

k1 = Kor(56)
print("A t1 kerülete: {0}, területe: {1}".format(k1.getKerulet(), k1.getTerulet()))

k1.setA(12)
print(f"A t1 kerülete: {k1.getKerulet()}, területe: {k1.getTerulet()}")


k2 = Negyzet(65)
print(f"A t2 kerülete: {k2.getKerulet()}, területe: {k2.getTerulet()}")