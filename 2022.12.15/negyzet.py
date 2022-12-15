from classes import *

n1 = Negyzet(56)
print("A t1 kerülete: {0}, területe: {1}".format(n1.getKerulet(), n1.getTerulet()))

n1.setA(12)
print(f"A t1 kerülete: {n1.getKerulet()}, területe: {n1.getTerulet()}")


n2 = Negyzet(65)
print(f"A t2 kerülete: {n2.getKerulet()}, területe: {n2.getTerulet()}")

