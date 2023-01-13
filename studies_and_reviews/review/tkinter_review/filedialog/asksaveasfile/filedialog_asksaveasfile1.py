"""
Create a simple notepad where the user is able to open
and save a file.
"""
import tkinter as tk
from tkinter import filedialog


def click_open():
    
    text_area.delete("1.0", "end")
    
    file_path = filedialog.askopenfilename(
        filetypes=(
            ("text files", "*.txt"),
            ("all files", "*.*")
        )
    )
    
    if file_path == "":
        return
    else:
        file = open(file_path, 'r')
        text_area.insert("1.0", file.read())
        file.close()


def click_save():
    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[
            ("text files", ".txt"),
            ("markdown file", ".md"),
            ("all files", ".*")
        ]
    )

    if file is None:
        return
    else:
        text = str(text_area.get("1.0", "end"))
        file.write(text)
        file.close()


root = tk.Tk()

open_button = tk.Button(root, text="Open", command=click_open)
open_button.pack()

save_button = tk.Button(root, text="Save", command=click_save)
save_button.pack()

text_area = tk.Text(root, font=("Arial", 15))
text_area.pack()

root.mainloop()