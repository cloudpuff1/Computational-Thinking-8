###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1=codesters.Square(100,100,200,'thistle')
q2=codesters.Square(-100,100,200,'gold')
q3=codesters.Square(-100,-100,200,'crimson')
q4=codesters.Square(100,-100,200,'turquoise')

s1=codesters.Sprite("goldenspiral",100,100)
s1.set_size(0.35)
s2=codesters.Sprite("purple-flower",-100,-100)
s2.set_size(0.5)
s3=codesters.Sprite("corgi",100,-100)
s3.set_size(0.5)
s4=codesters.Sprite("cardinal",-100,100)
s4.set_size(0.5)

message1=codesters.Text("Garima",0,220,"red")
message2=codesters.Text("this is my message",0,-220,"black")