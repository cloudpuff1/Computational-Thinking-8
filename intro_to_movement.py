# Section 1 - Helper functions (DON'T CHANGE!!)
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

window = turtle.Screen()
window.tracer(0)

# Create a keypress function for the z key
# In the new keypress function:
# Pick a new image
# make a variable with its full name, like in create_sprite
# Call s1.shape with this name
# Bonus: create a function that given a image name (cat) returns the whole name
# image("cat") -> "/workspaces/Computational-Thinking-8/Images/cat.gif"
# def image(image_filename):
#    return f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"

# Section 2: Setup
set_background("castle")
s1 = create_sprite("fish",0,-200)
s2 = create_sprite("baseball",0,-100)
follow=False
timer=0
hile True
timer==5
cake_made=False

# Section 3: define movement controls

def image(image_filename):
	return f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"

def costume_change1():
	screen = turtle.Screen()
	screen.register_shape(image("cat"))
	s1.shape(image("cat"))
def costume_change2():
	screen = turtle.Screen()
	screen.register_shape(image("cat"))
	s1.shape(image("cat"))

	
	

def change_follow():
	global follow
	follow=not follow
	
	
def move_up():
	s1.setheading(90)
	s1.forward(10)
	print(follow)
	if follow==True:
		s2.setheading(90)
		s2.forward(10)
		
   	 
def move_down():
	s1.setheading(270)
	s1.forward(10)
	if follow==True:
		s2.setheading(270)
		s2.forward(10)
    
def move_left():
	s1.setheading(180)
	s1.forward(10)
	if follow==True:
		s2.setheading(180)
		s2.forward(10)
    
def move_right():    
	s1.setheading(0)
	s1.forward(10)
	if follow==True:
		s2.setheading(0)
		s2.forward(10)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")
window.onkeypress(move_left, "Left")
window.onkeypress(background_change, " ")

if ( ):
	window.onkeypress(change_follow, " ")


# Section 4: define other controls
# hide and show controls
def hide():
	s1.hideturtle()
def show():
	s1.showturtle()

if():
	timer+=1
	time.sleep(1)
if():
	cake_made=True


# Section 5: game loop
window.listen()
while True:
	time.sleep(0.01)
	window.update()
	if timer==5:
		break
	if cake_made:
		break




