"""
Make a listbox where the user can change its color.
"""
import tkinter as tk
from tkinter import colorchooser


def change_color():
    color = colorchooser.askcolor()[1]
    fruits.config(bg=color)


root = tk.Tk()

fruits = tk.Listbox(root, font=("Consantia", 20))
fruits.pack()

fruits.insert(1, "Apple")
fruits.insert(2, "Banana")
fruits.insert(3, "Lemon")
fruits.insert(4, "Orange")

change_color_button = tk.Button(root, text="Change color", 
                                font=("Consantia", 18), command=change_color)
change_color_button.pack()


root.mainloop()
