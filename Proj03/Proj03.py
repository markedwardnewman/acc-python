#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj03.py

from Proj03Runner import Runner
import turtle
import random

window = turtle.Screen()
turtle.setup(300,300)

rand = random.randrange(0,2) #get a random number
#set object's colors based on the random number
if(rand%2==0):
    #rand is even
    color01 = "red"
    color02 = "green"
else:
    #rand is odd
    color01 = "green"
    color02 = "red"

objA = Runner(color01) #create one object
objB = Runner(color02) #create a second object

#Call the run method on each object and unpack
# the tuple that is returned.
colorA,turtleA,yourName = objA.run()
colorB,turtleB,yourName = objB.run()

window.title(yourName)

#Manipulate the turtles to draw a picture.
turtleA.color(colorA)
turtleA.forward(50)
turtleA.circle(50)

turtleB.color(colorB)
turtleB.right(180)
turtleB.forward(50)
turtleB.circle(50)

tempTurtle = turtle.Turtle()
tempTurtle.shape("turtle")
tempTurtle.left(90)
tempTurtle.color(color01)
tempTurtle.stamp()

#Pause and wait for the user to dismiss the window.
window.mainloop()