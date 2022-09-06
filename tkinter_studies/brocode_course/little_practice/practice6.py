"""
Make an entry box that receives the user's name.
"""
import tkinter as tk


def submit():
    username = entry.get()
    print(f'Hello, {username}!')


window = tk.Tk()

window.geometry('720x420')

label_text = 'Enter your username:'

label = tk.Label(window, text=label_text, font=('Arial', 20))
entry = tk.Entry(window, font=('Arial', 30))
submit_button = tk.Button(window, text='Submit', font=('Arial', 20), command=submit)

label.grid(column=0, row=0, pady=10)
entry.grid(column=0, row=1, padx=10, pady=10)
submit_button.grid(column=1, row=1, padx=10, pady=10)

window.mainloop()
