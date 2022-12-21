"""
Recreate study1.py
"""
import tkinter as tk
import time
from ball_practice import Ball

WIDTH = 500
HEIGHT = 500

window = tk.Tk()

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

test_ball = Ball(canvas=canvas, x=0, y=0, diameter=30, xvelocity=15, yvelocity=20, color="white")
basket_ball = Ball(canvas=canvas, x=0, y=0, diameter=70, xvelocity=10, yvelocity=14, color="orange")
tennis_ball = Ball(canvas=canvas, x=0, y=0, diameter=40, xvelocity=18, yvelocity=20, color="green")

while True:
    test_ball.move()
    basket_ball.move()
    tennis_ball.move()
    window.update()
    time.sleep(0.1)

window.mainloop()
