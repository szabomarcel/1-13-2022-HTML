import turtle

screen = turtle.Screen()
toll = turtle.Turtle()
#(n-2) * 180 - belső szögek összege
#(n-2) * 180/n - egy szög

def sokszog_rajzolas(t,n,sz):
   szog = (n-2) * 180/n
   for i in range(0,n):
      t.left(180 - szog)
      t.forward(sz)


sokszog_rajzolas(toll, 8, 50)

screen.mainloop()