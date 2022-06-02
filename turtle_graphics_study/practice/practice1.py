"""
Create several triangles on the screen. The triangles should have different sizes.
"""
import turtle
from random import randint


def triangle(ttle, size):
    ttle.begin_fill()
    for _ in range(3):
        ttle.forward(size)
        ttle.left(120)
    ttle.end_fill()


def random_position(ttle):
    ttle.penup()
    ttle.setpos(randint(-350, 300), randint(-300, 250))
    ttle.pendown()


def triangle_quantity(ttle, qtt=100, size=100):
    for _ in range(qtt):
        triangle(ttle, randint(0, size))
        random_position(ttle)


tt = turtle.Turtle()
turtle.bgcolor('#7C788B')
tt.speed(0)
tt.color('yellow', 'purple')

triangle_quantity(tt, 100)



turtle.done()
