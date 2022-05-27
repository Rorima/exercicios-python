import turtle
import math

tt = turtle.Turtle()
tt.color('red')
tt.speed(0)

for i in range(2000):
    tt.forward(math.sqrt(i))
    tt.left(i % 180)

turtle.done()