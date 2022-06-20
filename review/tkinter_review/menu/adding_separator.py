"""
Use add_separator()
"""
import tkinter as tk

window = tk.Tk()
menubar = tk.Menu(window)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
edit_menu = tk.Menu(menubar, tearoff=False)
help_menu = tk.Menu(menubar, tearoff=False)

file_menu.add_command(label="New")
file_menu.add_command(label="Open...")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="Help", menu=help_menu)

window.mainloop()
