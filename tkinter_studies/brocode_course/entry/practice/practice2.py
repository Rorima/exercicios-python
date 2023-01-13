"""
Create a program that receveis the name of
a user and and when they submit it, the entrybox
is disabled.
"""
import tkinter as tk


def submit():
    print(entry.get())
    entry.config(state='disabled')
    button.config(state='disabled')


window = tk.Tk()

entry = tk.Entry(window, font=('Arial', 20))
entry.insert(0, 'Type your username')
entry.pack(side='left')

button = tk.Button(window, text='Submit', font=('Arial', 15), command=submit)
button.pack(side='right')

window.mainloop()
