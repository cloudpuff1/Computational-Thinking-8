import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")
y=-61.56

# move to rectangle 
t.goto(-250, -100)

# rectangle 1
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(249.86)
t.left(90)
t.forward(500)
t.left(90)
t.forward(249.86)
t.left(90)
t.end_fill()


for i in range(6):
# stripes


    # move to stripe place
    t.goto(-250, y)

    # stripe 
    t.color("white")
    t.begin_fill()
    t.forward(500)
    t.left(90)
    t.forward(-19.22)
    t.left(90)
    t.forward(500)
    t.left(90)
    t.forward(-19.22)
    t.left(90)
    t.end_fill()
    y+=38.44

    
t.goto(-250,149.86)

# blue rectangle 
t.color("blue")
t.begin_fill()
t.forward(240)
t.left(90)
t.forward(-134.54)
t.left(90)
t.forward(240)
t.left(90)
t.forward(-134.54)
t.left(90)
t.end_fill()

turtle.exitonclick()
