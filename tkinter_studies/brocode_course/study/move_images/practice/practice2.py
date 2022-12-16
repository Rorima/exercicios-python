"""
Review study2
"""
import tkinter as tk


def move_up(event):
    canvas.move(ball, 0, -10)


def move_down(event):
    canvas.move(ball, 0, 10)


def move_left(event):
    canvas.move(ball, -10, 0)


def move_right(event):
    canvas.move(ball, 10, 0)


root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

ball_img = tk.PhotoImage(file="programas/study/move_images/ball.png")
ball = canvas.create_image(0, 0, image=ball_img, anchor="nw")

root.bind("w", move_up)
root.bind("s", move_down)
root.bind("a", move_left)
root.bind("d", move_right)

root.mainloop()
