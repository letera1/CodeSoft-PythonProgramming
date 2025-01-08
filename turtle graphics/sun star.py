from turtle import*
bgcolor('black')
pencolor('red')
pensize(5)
speed(0)
begin_fill()
fillcolor('yellow')
for  i   in  range(12):          
           for j in range(4):
               forward(150)
               left(90) 
           left(30)
end_fill()
pencolor('yellow')
dot(25)

hideturtle()