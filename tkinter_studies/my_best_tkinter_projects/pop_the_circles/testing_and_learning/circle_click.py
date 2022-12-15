"""
My main objective with this is to get the coords of the circle only.

"""
import tkinter as tk

START= 0
DIMENSION= 100


def show_coords(event):
    x = event.x
    y = event.y
    
    if (x > START) and (x < DIMENSION) and (y > START) and (y < DIMENSION):
        print(f"({x}, {y})")


root = tk.Tk()

c = tk.Canvas(root, width=500, height=500)
c.pack()

c.create_oval(START, START, DIMENSION, DIMENSION)
c.bind("<Button-1>", show_coords)

root.mainloop()
