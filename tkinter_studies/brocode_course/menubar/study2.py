import tkinter as tk

root = tk.Tk()
root.title("Menu Demo")

# create a menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = tk.Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label="Exit",
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)

root.mainloop()
