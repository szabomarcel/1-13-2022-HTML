import turtle

screen = turtle.Screen()
tek = turtle.Turtle()

def rajz(te, tab):
   for v,k in tab:
      te.right(v)
      te.forward(k)

table = [(180,100), (90,100), (90,100), (90,100), (135, 140), (90, 70), (90, 70), (90, 140)]
rajz(tek, table)
screen.mainloop()