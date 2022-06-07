"""
Use the dot and stamp methods.
"""

import turtle as tt
from random import randint, choice

colors = ["blue", "purple", "yellow", "green", "black", "red"]


tim = tt.Turtle()

direction = [tim.left, tim.right]

for _ in range(20):
    tim.fd(randint(1, 40))
    turning = choice(direction)
    turning(randint(0, 90))
    
    if randint(0, 1):
        tim.dot(20, choice(colors))
    else:
        tim.color(choice(colors))
        tim.stamp()


tt.done()
