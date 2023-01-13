"""
Create buttons with texts in them and make them the same size.
"""
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")

frame = tk.Frame(window)

button1 = tk.Button(frame, text="This is", padx=15).grid(row=0, column=0, ipadx=25)
button2 = tk.Button(frame, text="a little test").grid(row=0, column=1, ipadx=25)
button3 = tk.Button(frame, text="I'm doing.").grid(row=0, column=2, ipadx=25)
button4 = tk.Button(frame, text="Hopefully it will work.", padx=90).grid(row=1, column=0, columnspan=3, ipadx=25)

frame.pack(expand=True)

window.mainloop()
