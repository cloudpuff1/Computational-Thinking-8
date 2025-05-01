# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
    image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite = turtle.Turtle()
    sprite.shape(image_file)
    sprite.penup()
    sprite.goto(x,y)
    return sprite


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 =-200
y1 =200
x2 =-200
y2 =50
x3 =-200
y3 =-50
x4 =-200
y4 =-150
n1=random.randint(4,6)
n2=random.randint(3,6)
n3=random.randint(2,6)
n4=random.randint(1,6)

p1=random.randint(7,20)
p2=random.randint(9,20)
p3=random.randint(8,20)
p4=random.randint(6,20)



# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("castle")
t1 = create_sprite("cat2",x1,y1)
t2 = create_sprite("fish",x2,y2)
t3 = create_sprite("flower",x3,y3)
t4 = create_sprite("fox",x4,y4)


# Section 4 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - explain here which sprites are faster or slower so I won't know because I made the vaules for the increase in x random so i have all the varibles that random between number <6, and 6 and for all the varibles that have a p are random between a number <20, >6 and 20
for i in range(30):
    x1 +=random.randint(n1,p1)
    x2 +=random.randint(n2,p2)
    x3 +=random.randint(n3,p3)
    x4 +=random.randint(n4,p4)
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    time.sleep(0.1)


# Section 5 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("Cat wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print( "Fish wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("Flower wins!")
elif  x4 >= x1 and x4 >= x2 and x4 >= x4:
     print("Fox wins!")

turtle.exitonclick()
