"""
Create a model of the program.
"""
import tkinter as tk

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
    selectmode="extended"
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

done_button = tk.Button(
    button_frame, 
    font=("", 18),
    text="Check"
)
done_button.pack()

root.mainloop()
