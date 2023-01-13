import tkinter as tk


def open_file():
    print("File has been opened!")


def save_file():
    print("File has been saved!")


def cut():
    print("You cut some text!")


def copy():
    print("You copied some text!")


def paste():
    print("You pasted some text!")


root = tk.Tk()

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = tk.Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

root.mainloop()
