import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()
szélesség = 20
screen.bgcolor("black") 
teknos.color("green")

def Rajzol(szélesség):
   teknos.pendown()
   for i in range(0,4):
      teknos.left(90)
      teknos.forward(szélesség)
   teknos.penup()
      
def Újpoz():
   for i in range(0,2):
      teknos.forward(10)
      teknos.right(90)
   teknos.right(180)

for i in range(0,5):
   Rajzol(szélesség)
   Újpoz()
   szélesség += 20

screen.mainloop()