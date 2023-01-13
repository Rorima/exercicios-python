"""
Create a program where you can check the
activities you have completed for the day.

"""
import tkinter as tk
from typing_extensions import IntVar


def all_checked():
    checked = [a.get(), b.get(), c.get(), d.get()]
    if sum(checked) == 4: print('All checked')


window = tk.Tk()

window.resizable(False, False)
window.geometry("300x300")
window.title('Activities')

a = tk.IntVar()
b = tk.IntVar()
c = tk.IntVar()
d = tk.IntVar()

title = tk.Label(window,
                 text='Activities:',
                 font=('Comics', 30, 'bold'))

study = tk.Checkbutton(window,
                       text='Study',
                       font=('Comics', 20),
                       variable=a,
                       command=all_checked)

practice = tk.Checkbutton(window,
                          text='Practice',
                          font=('Comics', 20),
                          variable=b,
                          command=all_checked)

read = tk.Checkbutton(window,
                      text='Read',
                      font=('Comics', 20),
                      variable=c,
                      command=all_checked)

eat = tk.Checkbutton(window,
                     text='Eat',
                     font=('Arial', 20),
                     variable=d,
                     command=all_checked)


title.grid(row=0, column=0)
study.grid(row=1, column=0, sticky='w')
practice.grid(row=2, column=0, sticky='w')
read.grid(row=3, column=0, sticky='w')
eat.grid(row=4, column=0, sticky='w')

all_checked()

window.mainloop()
