"""
Make a drawing game.

Controls:
Arrows for movement;
h to hide or show the turtle;
Space for pen up or pen down.
"""

import turtle as tt

hidden = False


def go_up():
    tt.seth(90)
    tt.fd(10)


def go_right():
    tt.seth(0)
    tt.fd(10)


def go_left():
    tt.seth(180)
    tt.fd(10)


def go_down():
    tt.seth(270)
    tt.fd(10)


def on_paper():
    if tt.isdown():
        tt.up()
    else:
        tt.down()


def hide():
    global hidden

    if not hidden:
        tt.ht()
        hidden = True
    else:
        tt.st()
        hidden = False


tt.color("white")
tt.bgcolor("#646464")

tt.onkey(go_up, "Up")
tt.onkey(go_right, "Right")
tt.onkey(go_left, "Left")
tt.onkey(go_down, "Down")
tt.onkey(on_paper, " ")
tt.onkey(hide, "h")

tt.listen()
tt.done()
