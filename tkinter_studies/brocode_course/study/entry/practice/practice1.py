"""
Create an entrybox with the default text set to
'Username'.The background of your window and
entrybox should be black, and the text should
be green.
"""
import tkinter as tk


def submit():
    print(entry.get())


window = tk.Tk()

window.config(background='black')

entry = tk.Entry(window,
                 font=('Arial', 30),
                 fg='#00FF00',
                 bg='black')
entry.insert(0, 'Username')

entry.pack(side='left')

button = tk.Button(window,
                text='Submit',
                font=('Arial', 15),
                fg='#00FF00',
                bg='black',
                command=submit)
button.pack(side='right')

window.mainloop()
