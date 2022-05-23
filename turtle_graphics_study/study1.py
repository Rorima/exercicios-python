import turtle as tt

bob = tt.Turtle()


for _ in range(4):
    for _ in range(8):
        bob.forward(50)
        bob.left(45)
    bob.right(90)
    bob.forward(100)

tt.done()