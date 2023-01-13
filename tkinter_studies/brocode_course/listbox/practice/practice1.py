"""
Make a list box where the user is able to add and delete items.
"""
import tkinter as tk


def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())
    entrybox.delete(0, len(entrybox.get))


def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = tk.Tk()
window.title("Food")

listbox = tk.Listbox(window,
                     font=("Constantia", 20),
                     fg="#282727",
                     bg="#fdffde",
                     width=12)
listbox.pack()

listbox.insert(1, "Rice")
listbox.insert(2, "Beans")
listbox.insert(3, "Meat")
listbox.insert(4, "Chicken")

listbox.config(height=listbox.size())

entrybox = tk.Entry(window,
                    font=('Constantia', 10))
entrybox.pack()

add_button = tk.Button(window,
                       text="Add",
                       command=add)
add_button.pack()

delete_button = tk.Button(window,
                          text="Delete",
                          command=delete)
delete_button.pack()

window.mainloop()