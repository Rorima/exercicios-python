import tkinter as tk


def do_something(event):
    # print(f"You pressed {event.keysym}.")
    label.config(text=event.keysym)


window = tk.Tk()

window.bind("<Key>", do_something)
label = tk.Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
