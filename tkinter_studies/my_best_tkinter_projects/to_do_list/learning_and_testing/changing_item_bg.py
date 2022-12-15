"""
https://stackoverflow.com/questions/36914176/changing-colour-of-item-in-tkinter-listbox
Changing color of an item
"""
import tkinter as tk


already_colored = set()

def check():
    """Make the selected item green, but if it's already
    green, make it white again."""

    # Iterating through the selected items
    for item in listbox.curselection():

        # Getting the item name
        item_name = listbox.get(item)

        if item_name in already_colored:
            listbox.itemconfig(item, bg="white")
            # Bacause the item is white, it shouldn't be in the set anymore
            already_colored.discard(item_name)
        else:
            # Make the item green if it isn't in the set
            listbox.itemconfig(item, bg="#b7ec78")
            # Adding the item name into the set
            already_colored.add(item_name)
    
    # Unselecting the items
    listbox.selection_clear(0, "end")


root = tk.Tk()
root.geometry("500x500")

list_frame = tk.Frame(root, bg="blue")
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(
    list_frame,
    width=30,
    height=10,
    font=("times new romans", 20),
    yscrollcommand=scrollbar.set, 
    selectmode="multiple"
)
listbox.pack()

scrollbar.config(command=listbox.yview)

name_list = [
    "Adam", "Eve", "Cain", 
    "Abel", "Seth", "Enosh", 
    "Kenan", "Mahalalel", "Jared", 
    "Enoch", "Methuselah", "Lamech", 
    "Noah"
]

for name in name_list:
    listbox.insert("end", name)

button_frame = tk.Frame(root)
button_frame.pack(pady=40)

add_button = tk.Button(
    button_frame, 
    font=("", 18),
    text="Add"
)
add_button.pack(side="left", padx=10)

check_button = tk.Button(
    button_frame, 
    font=("", 18),
    text="Check",
    command=check
)
check_button.pack()

root.mainloop()
