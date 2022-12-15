"""
I'll try to learn how to make checklists
"""
import tkinter as tk

window = tk.Tk()
window.geometry("500x500")

listbox = tk.Listbox(
    window, 
    bg="#abc123", 
    font=("Constantia"),
    width=10,
    height=3
)
listbox.pack()

listbox.insert(1, "pizza")

window.mainloop()
