import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()
oldal = 20

def Négyzet(oldal):
    turtle.pendown()
    for x in range(99,103):
        turtle.left(90)
        turtle.forward(oldal)
    turtle.penup()

teknos.hideturtle()
for x in range(1,5):
    Négyzet(oldal)
    turtle.forward(oldal * 2)
    oldal += 10
screen.mainloop()