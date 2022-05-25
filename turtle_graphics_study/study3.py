import turtle

bob = turtle.Turtle()

bob.begin_fill()
for _ in range(4):
    bob.left(90)
    bob.forward(100)

bob.penup()
bob.forward(100)
bob.pendown()

for _ in range(4):
    bob.forward(100)
    bob.left(90)

bob.right(90)
bob.penup()
bob.forward(100)
bob.pendown()

for _ in range(4):
    bob.forward(100)
    bob.left(90)

bob.right(90)
bob.penup()
bob.forward(100)
bob.pendown()

for _ in range(4):
    bob.forward(100)
    bob.left(90)
bob.end_fill()

turtle.done()