import turtle as tr

s = tr.Screen()
tr.setup(800, 800)
s.bgcolor('#262626')
tr.speed(0)
tr.tracer(100)

col = ['red', 'yellow', 'white', 'black']

for n in range(400):
    tr.color(col[n % 4])
    tr.circle(190 - n / 2, 90)
    tr.left(90)
    tr.circle(190 - n / 2, 90)
    tr.left(30)

s.exitonclick()