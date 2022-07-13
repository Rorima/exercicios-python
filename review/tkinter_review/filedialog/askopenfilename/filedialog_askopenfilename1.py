"""
Create a progam that opens a file, reads it and places the text
inside a textbox.
"""
import tkinter as tk
from tkinter import filedialog


def click_open():
    file_path = filedialog.askopenfilename(filetypes=(("text file", "*.txt"),
                                                      ("all files", "*.*")))
    if file_path == "":
        return
    else:
        file = open(file_path, 'r')
        textbox.insert("1.0", file.read())
        file.close()


root = tk.Tk()

textbox = tk.Text(root)
textbox.pack()

open_button = tk.Button(root, text="open", command=click_open)
open_button.pack()

root.mainloop()
