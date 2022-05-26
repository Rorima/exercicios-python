"""
Drawing a flower.
"""
import turtle

tt = turtle.Turtle()
tt.speed(10)

tt.color('red', 'yellow')

tt.begin_fill()
for _ in range(36):
    tt.forward(300)
    tt.right(170)
tt.end_fill()

turtle.done()
