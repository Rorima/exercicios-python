"""
Trying to think how to start and stop the after method.
This is the first step.
"""
import tkinter as tk

opposite = False


def display_opposite():
    global opposite
    opposite = not opposite
    print(opposite)


root = tk.Tk()

b = tk.Button(root, command=display_opposite)
b.pack(fill="both")

root.mainloop()
