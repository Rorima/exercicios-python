from audioop import reverse
import tkinter as tk


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    for item in food:
        print(item, end=', ')


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())


window = tk.Tk()

listbox = tk.Listbox(window,
                     bg="#f7ffde",
                     font=("Constantia", 35),
                     width=12,
                     height=8,
                     selectmode="multiple")
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entry_box = tk.Entry(window)
entry_box.pack()


submit_button = tk.Button(window,
                          text="Submit",
                          command=submit)
submit_button.pack()

add_button = tk.Button(window,
                          text="Add",
                          command=add)
add_button.pack()

delete_button = tk.Button(window,
                          text="Delete",
                          command=delete)
delete_button.pack()

window.mainloop()
