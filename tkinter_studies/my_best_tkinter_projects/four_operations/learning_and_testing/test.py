import tkinter as tk

window = tk.Tk()
window.geometry("500x500")


photo = tk.PhotoImage(file="addition_operator.png")

b = tk.Button(
    window, 
    text="Text", 
    font=("", 30, "bold"),
    image=photo,
    compound="left"
)
b.pack(expand=True, ipadx=30)

window.mainloop()