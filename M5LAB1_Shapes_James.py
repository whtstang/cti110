import turtle             
win = turtle.Screen()      
jj = turtle.Turtle()
jj.shape("turtle")
jj.color("red")

for s in range(4):
    jj.forward(80)
    jj.left(90)

jj.penup()
jj.forward(100)
jj.pendown()

for t in range(3):
    jj.forward(100)
    jj.left(120)


win.mainloop()             
