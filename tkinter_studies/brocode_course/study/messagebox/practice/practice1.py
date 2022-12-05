"""
Make a program that displays a list of tools to the user and lets
them delete any item from the list, but a warning messagebox should
pop up asking if the user really wants to delete that item.
"""


def delete_func():

    item = tools.get(tools.curselection())
    msg=f"Are you sure you want to delete {item}?"
    
    answer = messagebox.askyesno(title="Deletion Warning!", message=msg)
    
    if answer:
        tools.delete(tools.curselection())
    else:
        pass


import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

tools = tk.Listbox(window, font=("Constantia", 20), width=15)
tools.pack()

tools.insert(1, "Hammer")
tools.insert(2, "Wrench")
tools.insert(3, "Pliers")
tools.insert(4, "Drill")

tools.config(height=tools.size())

delete_button = tk.Button(window, text="Delete", font=("Constantia", 20), command=delete_func)
delete_button.pack()

window.mainloop()
