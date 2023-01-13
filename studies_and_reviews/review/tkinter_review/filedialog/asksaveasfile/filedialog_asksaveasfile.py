"""
Create a program where the user is able to save a text file
they have created.
"""
import tkinter as tk
from tkinter import filedialog


def save():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=(("text files", ".txt"),
                                               ("markdown files", ".md"),
                                               ("all files", ".*")))
    if file == None:
        return
    filetext = textbox.get("1.0", "end")
    file.write(filetext)
    file.close()


root = tk.Tk()

textbox = tk.Text(root)
textbox.pack()

save_button = tk.Button(root, text="save", command=save)
save_button.pack()

root.mainloop()
