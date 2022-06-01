import turtle


def star(obj, size):
    if size <= 10:
        return
    else:
        obj.begin_fill()
        for _ in range(5):
            obj.forward(size)
            star(obj, size / 3)
            obj.left(216)
        obj.end_fill()


turtle.bgcolor('#df6259')

stars = turtle.Turtle()

stars.penup()
stars.goto((-170, 50))
stars.pendown()

stars.color('yellow')
stars.speed(0)

star(stars, 300)

turtle.done()
