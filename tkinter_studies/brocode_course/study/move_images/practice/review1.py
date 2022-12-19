"""
Reviewing study1.
"""
import tkinter as tk


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 5)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 5)

def move_right(event):
    label.place(x=label.winfo_x() + 5, y=label.winfo_y())

def move_left(event):
    label.place(x=label.winfo_x() - 5, y=label.winfo_y())


window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)

ball = tk.PhotoImage(file="programas/study/move_images/ball.png")

label = tk.Label(window, image=ball)
label.place(x=0, y=0)

window.bind("w", move_up)
window.bind("s", move_down)
window.bind("d", move_right)
window.bind("a", move_left)

window.mainloop()
