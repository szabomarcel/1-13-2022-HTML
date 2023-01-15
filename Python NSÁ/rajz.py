import turtle
turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("red")
for i in range(400):
    squary.forward(i)
    squary.left(91)

for i in range(180):
    squary.forward(300)
    squary.left(121)