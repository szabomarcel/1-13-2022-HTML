import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()

def poligon_rajzolas(t, sz):
    n = 360/sz
    for i in range(0,int(n)):
        teknos.forward(50)
        teknos.left(sz)

poligon_rajzolas(teknos, 120)

screen.mainloop()