"""
Create a program that opens a text file and then reads it, inserting
the text on a Text Widget.
"""
import tkinter as tk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Micro\\Desktop")
    file = open(file_path, 'r')
    text_area.insert("1.0", file.read())
    file.close()


root = tk.Tk()

text_area = tk.Text(
    root,
    font=("Arial", 20),
    height=15,
    width=40
)

text_area.pack()

open_button = tk.Button(
    root,
    text="Open",
    command=open_file
)
open_button.pack()

root.mainloop()
