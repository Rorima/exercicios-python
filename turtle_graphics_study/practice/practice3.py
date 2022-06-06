"""
Use the circle function to make a face.
"""

import turtle as tt


def face(ttl):
    ttl.color("black", "yellow")
    
    ttl.penup()
    ttl.sety(-200)
    ttl.pendown()

    ttl.begin_fill()
    ttl.circle(200)
    ttl.end_fill()


def smile(ttl):
    ttl.color("black", "white")
    
    setting_position_for_smile(ttl)

    ttl.begin_fill()
    lower_smile(ttl)
    upper_smile(ttl)
    ttl.end_fill()


def setting_position_for_smile(ttl):
    ttl.penup()
    ttl.goto(-120.00,-50.00)
    ttl.seth(270)
    ttl.pendown()


def lower_smile(ttl):
    ttl.circle(120, 180)


def upper_smile(ttl):
    ttl.seth(225)
    ttl.circle(-170, 90)


def eyes(ttl):
    ttl.color("black", "white")

    # Right eye
    ttl.penup()
    ttl.seth(0)
    ttl.goto(70.00, -0.00)
    ttl.pendown()

    ttl.begin_fill()
    ttl.circle(50)
    ttl.end_fill()

    # Left eye
    ttl.penup()
    ttl.seth(180)
    ttl.goto(-70.00, 0.00)
    ttl.pendown()
    
    ttl.begin_fill()
    ttl.circle(-50)
    ttl.end_fill()

    center(ttl)


def center(ttl):
    ttl.penup()
    ttl.home()
    ttl.seth(90)
    ttl.pendown()


bob = tt.Turtle()
bob.speed(0)

face(bob)
smile(bob)
eyes(bob)


tt.done()
