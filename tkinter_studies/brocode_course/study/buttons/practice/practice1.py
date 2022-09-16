"""
Create a program that doesn't change the color
when a button is pressed.
"""
import tkinter as tk

counter = 0


def click():
    global counter
    counter += 1
    print(counter)


window = tk.Tk()

button = tk.Button(window,
                   text='Click me!',
                   font=('Arial', 30),
                   fg='#00ff00',
                   bg='black',
                   activeforeground='#00ff00',
                   activebackground='black',
                   command=click)
button.pack()

window.mainloop()
