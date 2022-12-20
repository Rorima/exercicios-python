import tkinter as tk
import time
from Ball import Ball

WIDTH = 500
HEIGHT = 500

window = tk.Tk()

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 60, 13, 10, "blue")
tennis_ball = Ball(canvas, 0, 0, 30, 20, 14, "yellow")
basket_ball = Ball(canvas, 0, 0, 90, 15, 12, "orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.1)

window.mainloop()
