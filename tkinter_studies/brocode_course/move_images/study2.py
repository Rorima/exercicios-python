import tkinter as tk


def move_up(event):
    canvas.move(ball, 0, -10)

def move_down(event):
    canvas.move(ball, 0, 10)

def move_left(event):
    canvas.move(ball, -10, 0)

def move_right(event):
    canvas.move(ball, 10, 0)


window = tk.Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Remember to change the path
ball_img = tk.PhotoImage(file="programas/study/move_images/ball.png")
ball = canvas.create_image(0, 0, image=ball_img, anchor="nw")

window.mainloop()
