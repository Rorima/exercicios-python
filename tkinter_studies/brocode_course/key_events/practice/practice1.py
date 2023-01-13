"""
Create a program that quits if the user presses "q".
"""
from tkinter import *


def destroy_window(event):
    root.destroy()


root = Tk()
root.geometry("600x400")

root.bind("<q>", destroy_window)
Label(root, text="Press 'q' to close the window.", font=("Arial", 20)).pack(expand=True)

root.mainloop()
