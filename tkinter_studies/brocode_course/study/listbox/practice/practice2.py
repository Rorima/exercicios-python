"""
Create a lisbox where one is able to select multiple items
and delete multiple items.
"""
import tkinter as tk


def delete_item():
    for i in reversed(food_listbox.curselection()):
        food_listbox.delete(i)
    food_listbox.config(height=food_listbox.size())


window = tk.Tk()

food_listbox = tk.Listbox(window,
                          font=("Constantia", 20),
                          width=12,
                          selectmode="multiple")
food_listbox.pack()

food_listbox.insert(1, "Eggs")
food_listbox.insert(2, "Bread")
food_listbox.insert(3, "Butter")
food_listbox.insert(4, "Peanut butter")
food_listbox.insert(5, "Jam")
food_listbox.insert(6, "Cheese")

food_listbox.config(height=food_listbox.size())

delete_button = tk.Button(window, text="Delete", 
                          font=("Constantia", 20), command=delete_item)
delete_button.pack()

window.mainloop()
