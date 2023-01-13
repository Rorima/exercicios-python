"""
Create a menubar with file, open and save buttons. Create another one named
"edit", and another one named "preferences". They don't need to have
a function associated to them.
"""
import tkinter as tk

window = tk.Tk()

menubar = tk.Menu(window)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Exit", command=window.destroy)

edit_menu = tk.Menu(menubar, tearoff=False)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

preferences_menu = tk.Menu(menubar, tearoff=False)
preferences_menu.add_command(label="Resize")
preferences_menu.add_command(label="Change theme")
preferences_menu.add_command(label="Change font")

menubar.add_cascade(
    label="File",
    menu=file_menu
)
menubar.add_cascade(
    label="Edit",
    menu=edit_menu
)
menubar.add_cascade(
    label="Preferences",
    menu=preferences_menu
)

window.mainloop()
