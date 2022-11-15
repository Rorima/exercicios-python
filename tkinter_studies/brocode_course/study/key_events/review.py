import tkinter as tk


def display_key(event):
    lb.config(text=event.keysym)


window = tk.Tk()
window.geometry("300x300")

window.bind("<Key>", display_key)

lb = tk.Label(window, font=("Arial", 30))
lb.pack(expand=True)


window.mainloop()
