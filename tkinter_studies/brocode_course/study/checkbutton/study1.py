import tkinter as tk


def test():
    if x.get() == 1:
        print('O Márcio clicou!')
    else:
        print('Ele clicou de novo!')


window = tk.Tk()


window.config(background='black')
window.geometry('300x300')

x = tk.IntVar()

check_button = tk.Checkbutton(window,
                              text='Marcinho',
                              font=('Arial', 20),
                              fg='#00FF00',
                              bg='black',
                              activeforeground='#00FF00',
                              activebackground='black',
                              variable=x,
                              command=test
                              )

check_button.pack(side='top')

window.mainloop()
