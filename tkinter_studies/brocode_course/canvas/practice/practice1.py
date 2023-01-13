"""
Create a shape using create_line method.
"""
from tkinter import *

root = Tk()

cnvs = Canvas(root, width=300, height=300)
cnvs.create_line(100, 100, 100, 200)  # Vertical left
cnvs.create_line(100, 200, 200, 200)  # Horizontal bottom
cnvs.create_line(200, 100, 200, 200)  # Vertical right
cnvs.create_line(100, 100, 200, 100)  # Horizontal top
cnvs.pack()


root.mainloop()
