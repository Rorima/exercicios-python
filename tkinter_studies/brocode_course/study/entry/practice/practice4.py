"""
Write a program that asks for the username and password.
The program should ask for the password twice, and if the
first is different from the second, it will not accept.
"""
import tkinter as tk


def submit():
    name = user_name_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    
    if confirm_password != password:
        confirm_password_entry.delete(0, 'end')
        confirm_password_entry.insert(0, "Passwords must match")
    else:
        user_name_entry.config(state='disabled')
        password_entry.config(state='disabled')
        confirm_password_entry.config(state='disabled')
        button.config(state='disabled')
        print(f'{name}\n'
              f'{password}')


window = tk.Tk()

user_name_entry = tk.Entry(window, font=('Arial', 25))
user_name_entry.insert(0, 'Username')
user_name_entry.pack()

password_entry = tk.Entry(window, font=('Arial', 25))
password_entry.insert(0, 'Password')
password_entry.pack()

confirm_password_entry = tk.Entry(window, font=('Arial', 25))
confirm_password_entry.insert(0, 'Repeat password')
confirm_password_entry.pack()

button = tk.Button(window, text='Submit', font=('Arial', 15), command=submit)
button.pack(side='right')

window.mainloop()
