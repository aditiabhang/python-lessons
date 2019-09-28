import turtle

wn = turtle.Screen() # creates a graphical window object
wn.bgcolor('black')

alex = turtle.Turtle() # creates an turtle object on which operations will be performed
alex.color('blue')
alex.pensize(2)

alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)

wn.exitonclick()