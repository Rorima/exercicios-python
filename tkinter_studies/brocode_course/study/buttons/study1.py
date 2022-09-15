import tkinter as tk

count = 0


def click():
    global count
    count += 1
    print(count)


window = tk.Tk()

photo = tk.PhotoImage(file='like.png')

button = tk.Button(window,
                   text='Click me!',
                   command=click,
                   font=('Comic Sans', 30),
                   fg='green',
                   bg='black',
                   activeforeground='green',
                   activebackground='black',
                   image=photo,
                   compound='bottom')
button.pack()

window.mainloop()
