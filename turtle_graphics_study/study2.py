import turtle

ron = turtle.Turtle()
ron.color('blue', 'purple')

ron.begin_fill()
for _ in range(4):
    ron.left(90)
    ron.forward(100)
ron.end_fill()


turtle.done()