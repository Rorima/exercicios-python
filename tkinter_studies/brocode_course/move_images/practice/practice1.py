"""
Make an image move on the screen and limit its
movement. Don't let it disappear from the screen
by going in any direction endlessly.
"""
import tkinter as tk


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 7)
    # limit the motion
    if label.winfo_y() < -14:
        label.place(x=label.winfo_x(), y=-19)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 7)
    # limit the motion
    if label.winfo_y() > 383:
        label.place(x=label.winfo_x(), y=385)


def move_left(event):
    label.place(x=label.winfo_x() - 7, y=label.winfo_y())
    # limit the motion
    if label.winfo_x() < -19:
        label.place(x=-21, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x() + 7, y=label.winfo_y())
    # limit the motion
    if label.winfo_x() > 380:
        label.place(x=385, y=label.winfo_y())


def show_coordinates(event):
    print(f"x={label.winfo_x()}, y={label.winfo_y()}")


window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)

# Remember to change
ball = tk.PhotoImage(file="programas/study/move_images/ball.png")

label = tk.Label(window, image=ball)
label.place(x=0, y=0)

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<c>", show_coordinates)

window.mainloop()
