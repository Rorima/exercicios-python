import tkinter as tk


def submit():
    username = entry.get()
    print(f"Hello, {username}!")


def delete():
    entry.delete(0, 'end')


def backspace():
    entry.delete(len(entry.get())-1, 'end')


window = tk.Tk()

# Entry
entry = tk.Entry(window,
                 font=('Arial', 50),
                 fg="#00FF00",
                 bg="black")
entry.insert(0, 'Spongebob')
entry.pack(side='left')

# Submit
submit_button = tk.Button(window,
                          text='Submit',
                          command=submit)
submit_button.pack(side='right')


# Delete
delete_button = tk.Button(window,
                          text='delete',
                          command=delete)
delete_button.pack(side='right')


# Backspace
backspace_button = tk.Button(window,
                          text='backspace',
                          command=backspace)
backspace_button.pack(side='right')

window.mainloop()
