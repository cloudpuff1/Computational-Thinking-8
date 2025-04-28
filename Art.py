
# ###############################################
# ### SETUP ### #
import turtle
# ###############################################
t = turtle.Turtle()
t.penup()
# ### STARTING_POSITION ### #
t.goto(-100,-100)
# ### SET_SPEED_TO_MAX ### #
t.speed(10)
# ### SETUP_COLORS ### #
t.color("purple")
turtle.Screen().bgcolor("black")
t.pendown()


colors=["purple","cyan","thistle","turquoise"]
# ### DRAW_SHAPE ### #
for i in range (40):
    t.color(colors[i%4])
    t.forward(100)
    t.left(35+6)

turtle.exitonclick()