import turtle
import random

tt = turtle.Turtle()
tt.speed(0)
tt.color('blue')

for _ in range(random.randint(1, 100)):
    tt.forward(random.randint(0, 50))
    tt.setheading(random.randint(0, 360))

turtle.done()
