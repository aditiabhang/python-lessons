import turtle

wn = turtle.Screen()
wn.bgcolor('black')

jon = turtle.Turtle()

colours = ['green', 'blue', 'red', 'orange']  

# looping will be done 4 tim
for c in colours:
    # jon.color(c)
    jon.forward(100)
    jon.left(90)

wn.exitonclick()

