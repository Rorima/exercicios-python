"""
Create a menu bar and add file and edit options to it.
Inside the "file" option, there should be a "open" and
"save as" options;
Inside the "edit" option, there should be a "cut", "copy"
and "paste" options.
"""
import tkinter as tk

window = tk.Tk()

menubar = tk.Menu(window)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save As")

edit_menu = tk.Menu(menubar, tearoff=False)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

menubar.add_cascade(label="File", menu=file_menu)

menubar.add_cascade(label="Edit", menu=edit_menu)

window.mainloop()
