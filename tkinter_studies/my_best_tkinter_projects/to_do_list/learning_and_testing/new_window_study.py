"""
If I close the root, the top disappears as well.
The toplevel window works just as the normal window,
so you can add labels, buttons and other things.
"""
from tkinter import *

root = Tk()
root.title("Root window")

top = Toplevel()
top.title("Top window")
lbl = Label(top, text="hello!").pack()

root.mainloop()