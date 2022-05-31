import turtle

turtle.bgcolor('#df6259')

stars = turtle.Turtle()
stars.color('yellow')
stars.speed(0)

for i in range(12):
    for _ in range(5):
        stars.forward(i*30)
        stars.right(144)

stars.setpos((0.0, 0.0))
stars.left(145)
for i in range(12):
    for _ in range(5):
        stars.forward(i*30)
        stars.right(144)



turtle.done()
