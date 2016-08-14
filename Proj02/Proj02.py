#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj02.py

from Proj02Runner import Runner
import turtle

window = turtle.Screen()
turtle.setup(300,200)

objA = Runner("red") #create one object
objB = Runner("green") #create a second object
#Call the run method on each object and unpack
# the tuple that is returned.
colorA,turtleA,yourName = objA.run()
colorB,turtleB,yourName = objB.run()

window.title(yourName)

#Manipulate the turtles to draw a picture.
turtleA.left(90)
turtleA.stamp()
turtleA.right(90)
turtleA.forward(50)
turtleA.right(30)
turtleA.color(colorA)
turtleA.forward(50)

turtleB.right(180)
turtleB.forward(50)
turtleB.left(30)
turtleB.color(colorB)
turtleB.forward(50)

#Pause and wait for the user to dismiss the window.
window.mainloop()
