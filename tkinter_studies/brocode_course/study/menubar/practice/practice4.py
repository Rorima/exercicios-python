"""
Reviewing:

Create a notepad with a menubar containing "File" and "Edit" options.

Inside the "File" there should be "New", "Open", "Save", "Save As" and
"Exit" options.
Inside the "Edit" there should be "Cut", "Copy", "Paste" and 
"Selection" options.
Inside "Selection" (which is a submenu), there should be "Selec All",
"Expand Selection" and "Shrink Selection".

None of these options need to be functional.
"""
import tkinter as tk

root = tk.Tk()

menubar = tk.Menu(root)
root.resizable(False, False)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
edit_menu = tk.Menu(menubar, tearoff=False)

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

selection_menu = tk.Menu(edit_menu, tearoff=False)
selection_menu.add_command(label="Select All")
selection_menu.add_command(label="Expand Selection")
selection_menu.add_command(label="Shrink Selection")

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_cascade(label="Selection", menu=selection_menu)

text_area = tk.Text(
    root, 
    font=("Arial", 15),
    height=15,
    width=60,
    padx=15,
    pady=15
)
text_area.pack()

root.mainloop()
