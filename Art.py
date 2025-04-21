
# ###############################################
# ### SETUP ###
import turtle
# ###############################################
t = turtle.Turtle()
t.penup()
t.goto(-100,-100)
t.speed(10)
t.color("purple")
turtle.Screen().bgcolor("black")
t.pendown()


colors=["purple","cyan","thistle","turquoise"]

for i in range (40):
    t.color(colors[i%4])
    t.forward(100)
    t.left(35+6)

turtle.exitonclick()