import turtle             
win = turtle.Screen()
win.bgcolor("blue")
jj = turtle.Turtle()
jj.shape("turtle")
jj.color("white")
jj.speed(2)

numSides = int(input("How amny sides in the snowflake?"))

angle = 360 / numSides
sides = range(numSides)
distance = 90

for i in sides:
    jj.forward(distance)
    jj.left(angle)

for in 

win.mainloop()
