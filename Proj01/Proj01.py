#DO NOT MODIFY THE CODE IN THIS FILE
#File: Proj01.py

from Proj01Runner import Runner
import turtle

window = turtle.Screen()
turtle.setup(450,450)

aTuple = (turtle.Turtle(),turtle.Turtle(),turtle.Turtle())

result = Runner.run(aTuple)

window.title(result[3]) #display your name

result.append(turtle.Turtle())
result[4].pensize(5)
result[4].color('cyan')
result[4].shape('square')

result[0].forward(25)
result[0].circle(25)

result[1].right(90.0)
result[1].forward(50)
result[1].circle(50)

result[2].right(180.0)
result[2].forward(75)
result[2].circle(75)

result[4].left(90.0)
result[4].forward(100)
result[4].circle(100)

#Pause and wait for the user to dismiss the window.
window.mainloop()
