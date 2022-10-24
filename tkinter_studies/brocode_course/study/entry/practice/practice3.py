"""
Make a program that receves the name and password of
a user.
"""
import tkinter as tk


def submit():
    print(name_entry.get())
    print(passwd_entry.get())
    name_entry.config(state='disabled')
    passwd_entry.config(state='disabled')
    button.config(state='disabled')


window = tk.Tk()

name_entry = tk.Entry(window, font=('Arial', 25))
name_entry.pack()

passwd_entry = tk.Entry(window, font=('Arial', 25), show='*')
passwd_entry.pack()

button = tk.Button(window, text='Submit', font=('Arial', 15), command=submit)
button.pack(side='right')

window.mainloop()
