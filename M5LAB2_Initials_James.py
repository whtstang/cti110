import turtle             
win = turtle.Screen()      
jj = turtle.Turtle()
jj.shape("turtle")
jj.color("blue")
jj.speed(2)

jj.right(90)
jj.forward(20)
jj.left(90)
jj.forward(40)
jj.left(90)
jj.forward(100)

jj.right(90)
jj.penup()
jj.forward(60)
jj.pendown()
jj.right(90)
jj.forward(100)
jj.right(90)
jj.forward(40)
jj.right(90)
jj.forward(20)

win.mainloop()