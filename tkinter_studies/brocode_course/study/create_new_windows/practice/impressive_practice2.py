"""
Create a Tk() window that will display a number.
The number should increase every time a new window is opened.

PS: WHAT
"""
import tkinter as tk

counter = 0


def create_window():
    global new_window, counter
    counter += 1
    new_window.destroy()
    new_window = tk.Tk()
    new_window.geometry("300x300")

    create_new_window = tk.Button(
        new_window,
        text="Click to create a new window",
        font=("Constantia", 15),
        command=create_window
    )
    create_new_window.pack()

    tk.Label(text=counter, font=("Constantia", 30)).pack()


new_window = tk.Tk()
new_window.geometry("300x300")

create_new_window = tk.Button(
    new_window,
    text="Click to create a new window",
    font=("Constantia", 15),
    command=create_window
)
create_new_window.pack()

new_window.mainloop()
