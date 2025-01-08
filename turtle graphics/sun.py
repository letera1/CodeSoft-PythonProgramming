from turtle import*
bgcolor('black')
pencolor('yellow')

penup()
goto(0,-100)
pendown()
begin_fill()

fillcolor('yellow')
circle(100)
end_fill()

penup()
goto(0,0)
pendown()

pensize(7)

speed(0)

for i in range(7):

     forward(200)

     backward(400)

     forward(200)

     left(27)
