"""
Create a program with a chapter of the Bible
"""
from tkinter import *
from practice5a import *

window = Tk()

nice_fg = '#f9f9f9'
nice_bg = '#ebebeb'

window.geometry('1120x700')
window.resizable(False, False)
window.title('Proverbs')
window.config(background=nice_bg)

proverbs_title = Label(text='PROVERBS 4',
                       font=('Arial', 20, 'bold'),
                       bg=nice_bg)

proverbs = Label(text=proverbs4,
                 font=('Arial', 14),
                 bg=nice_bg,
                 justify=LEFT)

left_button = Label(text='<',
                    font=('Arial', 30, 'bold'),
                    bg=nice_bg,
                    padx=20)

right_button = Label(text='>',
                    font=('Arial', 30, 'bold'),
                    bg=nice_bg,
                    padx=20)

proverbs_title.grid(column=2, row=1)
proverbs.grid(column=2, row=2)
left_button.grid(column=1, row=2)
right_button.grid(column=3, row=2)

window.mainloop()
