"""
Write a program that has a check button in it.

The background color of your window and check
button should be the same.

When the box is checked, the text should not
blink.

Add an image to the left side of the box's
text.

Add a variable to your check button that will
return a boolean value.

"""
import tkinter as tk


def display():
    print(checked.get())


window = tk.Tk()

checked = tk.BooleanVar()

python_image = tk.PhotoImage(file="python.png")

window.config(background='black')

check_button = tk.Checkbutton(window,
                              text='I agree to check the box',
                              font=('Comics', 20),
                              fg='#00FF00',
                              bg='black',
                              activeforeground='#00FF00',
                              activebackground='black',
                              variable=checked,
                              command=display,
                              image=python_image,
                              compound='left')
check_button.pack()

window.mainloop()
