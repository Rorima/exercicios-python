"""
Create a notepad with two buttons: open and save.
"""
import tkinter as tk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(filetypes=(
        ("text file", "*.txt"),
        ("markdown", "*.md"),
        ("all files", "*.*")
    ))
    file = open(file_path, 'r')
    text_area.insert("1.0", file.read())
    file.close()


def save_file():
    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("text file", ".txt"), 
                   ("markdown", ".md"), 
                   ("all files", ".*")]
    )

    file_text = str(text_area.get("1.0", "end"))
    file.write(file_text)
    file.close()


root = tk.Tk()

root.resizable(False, False)


open_button = tk.Button(
    root,
    text="Open",
    font=("Arial", 15),
    command=open_file
)
open_button.grid(sticky='w')

save_button = tk.Button(
    root,
    text="Save",
    font=("Arial", 15),
    command=save_file
)
save_button.grid(row=0, sticky='e')

text_area = tk.Text(
    root,
    font=("Arial", 20),
    height=15,
    width=50,
    padx=15,
    pady=15
)
text_area.grid()

root.mainloop()
