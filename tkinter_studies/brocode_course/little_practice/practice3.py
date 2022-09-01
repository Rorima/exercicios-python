"""
Create a raised widget with an image and a text.
"""
from tkinter import *

window = Tk()

window.geometry('300x300')
window.title('Practice3')
photo = PhotoImage(file='flower.png')

my_label = Label(text='Hi!',
                 font=('Roboto', 30, 'italic'),
                 fg='white',
                 bg='black',
                 image=photo,
                 compound='bottom',
                 relief=RAISED,
                 bd=5)

my_label.pack()

window.mainloop()
