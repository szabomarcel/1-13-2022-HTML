import turtle

class Rajz:
    width = -160
    def szamozas():
        y = 190
        for i in range(0,39):
            turtle.goto(-180,y)
            turtle.goto(-175,y)
            turtle.goto(-185,y)
            turtle.goto(-180,y)
            y -= 10

    def diagram(height):
        color = ""
        if height >=200:
            color = "red"
        elif height < 200 and height >= 100:
            color = "yellow"
        elif height < 100:
            color = "green"

        turtle.goto(Rajz.width,0)

        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.goto(Rajz.width,height)
        turtle.goto(Rajz.width + 10,height)
        turtle.goto(Rajz.width + 10,0)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(Rajz.width - 5,height + 5)
        turtle.write(" "+ str(height))
        Rajz.width += 20

screen = turtle.Screen()
t = turtle.turtles()
turtle.speed(100)

turtle.goto(200,0)
turtle.goto(-200,0)
turtle.goto(-180,0)
turtle.goto(-180,200)
turtle.goto(-180,-200)
Rajz.szamozas()
turtle.penup()

for i in range(0,int(input("Írd be hány darab grafikon lesz:"))):
    Rajz.diagram(int(input(f"Írd be az {i + 1}. grafikon nagysága: ")))
        
screen.mainloop()