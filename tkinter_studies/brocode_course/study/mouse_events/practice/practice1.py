"""
Create a label on the screen that shows the coordinates of a click.
"""
from tkinter import *


def show_coordinates(event):
    label.config(text=f"({event.x}, {event.y})")


root = Tk()
root.geometry("600x400")

root.bind("<Button-1>", show_coordinates)
label = Label(root, text="(0, 0)", font=("Arial", 40))
label.pack(expand=True)

root.mainloop()
