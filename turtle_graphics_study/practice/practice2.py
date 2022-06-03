"""
Use goto() and setheading()

Create a face where the eyes are two triangles.
"""
import turtle as tt


def triangle(tt):
    for _ in range(3):
        tt.forward(50)
        tt.left(120)


def center(tt):
    tt.penup()
    tt.home()
    tt.pendown()


def align_for_smile(tt):
    tt.penup()
    tt.setx(-10)
    tt.pendown()


def smile(tt):
    align_for_smile(tt)
    tt.right(50)
    for _ in range(5):
        tt.forward(30)
        tt.left(25)


def nose(tt):
    tt.penup()
    tt.setheading(90)
    tt.goto(52.95, 50.00)


kim = tt.Turtle()
kim.speed(0)
kim.color('blue')

kim.penup()
kim.goto(-100, 100)
kim.pendown()

triangle(kim)

kim.penup()
kim.goto(150, 100)
kim.pendown()

triangle(kim)

center(kim)

smile(kim)

nose(kim)

tt.done()
