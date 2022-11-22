import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()

def féloldal(t, hossz):
    t.forward(hossz)
    t.left(90)

def négyzet(t, oldal):
    for i in range(2):
        féloldal(t, oldal / 2)
        
    for i in range(3):
        féloldal(t, oldal)
    
    féloldal(t, oldal / 2)
    t.forward(oldal / 2)

for i in range(24): 
    négyzet(teknos, 50)
    teknos.left(15)

teknos.hideturtle()
screen.mainloop()