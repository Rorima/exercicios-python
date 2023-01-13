from tkinter import *

window = Tk()

photo = PhotoImage(file='flower.png')
label = Label(window,
              text='Hello, Father!',
              font=('Arial', 40, 'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')

label.pack()
window.config(background='black')

window.mainloop()
