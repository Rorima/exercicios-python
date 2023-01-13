"""
Create a program that reads a file and prints it.
"""
import tkinter as tk
from tkinter import filedialog


def click_read():
    file_path = filedialog.askopenfilename(filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if file_path == "":
        return
    file = open(file_path, 'r')
    print(file.read())
    file.close()
    


window = tk.Tk()

bt = tk.Button(window, text="open", command=click_read)
bt.pack()

window.mainloop()
