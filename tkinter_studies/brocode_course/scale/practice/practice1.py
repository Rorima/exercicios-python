"""
Create a volume slider and a button to send the desired volume.
"""
import tkinter as tk


def sender():
    print(f"The desired volume is {volume.get()}.")


window = tk.Tk()

window.config(background="black")
window.resizable(False, False)

volume = tk.Scale(window,
                  from_=100,
                  to=0,
                  length=500,
                  tickinterval=10,
                  troughcolor="#51dd00",
                  fg="#51dd00",
                  bg="black",
                  font=("Consola", 20, "bold"))
volume.set(50)
volume.pack()

send = tk.Button(window, 
                 text="Send",
                 font=("Consola", 20, "bold"),
                 fg="#51dd00",
                 bg="black",
                 activebackground="black",
                 activeforeground="#51dd00",
                 padx=20,
                 command=sender)
send.pack()

window.mainloop()