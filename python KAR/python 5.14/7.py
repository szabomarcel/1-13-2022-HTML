import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()
szélesség = 20

def osszeg(n):
    összegzés = 0
    for i in range(0,n+1):
        összegzés += i
    return összegzés

print(osszeg(20))
screen.mainloop()