import tkinter as tk

root = tk.Tk()

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)

file_menu.add_command(
    label="Exit",
    command=quit
)
file_menu.add_command(
    label="Open"
)
file_menu.add_command(
    label="Save"
)
file_menu.add_command(
    label="Save as"
)



edit_menu = tk.Menu(menubar, tearoff=False)

edit_menu.add_command(
    label="Cut"
)
edit_menu.add_command(
    label="Copy"
)
edit_menu.add_command(
    label="Paste"
)


menubar.add_cascade(
    label="File",
    menu=file_menu
)

menubar.add_cascade(
    label="Edit",
    menu=edit_menu
)
root.mainloop()
