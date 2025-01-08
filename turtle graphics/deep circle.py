from turtle import *

bgcolor('black')
pensize(4)

for i in range(26):
    color('yellow')
    forward(190)
    left(-90)
    circle(20, 90)

    penup()
    forward(100)
    goto(0, 0)
    pendown()
    right(15)
    backward(15)
    
