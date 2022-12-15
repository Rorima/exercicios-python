import tkinter as tk


def show_coords(event):
    x = event.x
    y = event.y
    print(f"You clicked ({x}, {y})")


window = tk.Tk()
window.geometry("500x500")

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

canvas.bind("<Button-1>", show_coords)

window.mainloop()
