import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()

def négyzet(oldal):
    for i in range(2):
        teknos.forward(oldal / 2)
        teknos.left(90)
    for i in range(3):
        teknos.forward(oldal)
        teknos.left(90)
    
    teknos.forward(oldal / 2)
    teknos.left(90)
    teknos.forward(oldal / 2)

for i in range(24): 
    négyzet(50)
    teknos.left(15)

teknos.hideturtle()
screen.mainloop()