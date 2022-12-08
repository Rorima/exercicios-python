import tkinter as tk


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 7)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 7)


def move_left(event):
    label.place(x=label.winfo_x() - 7, y=label.winfo_y())


def move_right(event):
    label.place(x=label.winfo_x() + 7, y=label.winfo_y())


window = tk.Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# Remember to change this
ball = tk.PhotoImage(file="programas/study/move_images/ball.png")
label = tk.Label(window, image=ball)
label.place(x=0, y=0)

window.mainloop()
