import tkinter as tk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Micro\\Desktop\\curso desenho")
    file = open(file_path, 'r')
    print(file.read())
    file.close()


root = tk.Tk()

open_button = tk.Button(
    text="Open",
    command=open_file
)
open_button.pack()


root.mainloop()
