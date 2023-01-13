import tkinter as tk
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()[1]
    root.config(background=color)


root = tk.Tk()

root.geometry("420x420")

bt = tk.Button(root, text="click me", command=click)
bt.pack()

root.mainloop()
