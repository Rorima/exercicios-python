import tkinter as tk


def submit():
    print(f"The temperature is: {scale.get()}°")


window = tk.Tk()

hotimage = tk.PhotoImage(file="programas\\study\\scale\\hot.png")
hotlabel = tk.Label(image=hotimage)
hotlabel.pack()

scale = tk.Scale(window, 
                 from_=100, 
                 to=0,
                 length=600,
                 font=("Arial", 20),
                 tickinterval=10,
                 troughcolor="#69EAFF",
                 fg="#FF1C00",
                 bg="black")

scale.set(100)
scale.pack()

coldimage = tk.PhotoImage(file="programas\\study\\scale\\cold.png")
coldlabel = tk.Label(image=coldimage)
coldlabel.pack()

button = tk.Button(window, 
                   text="Submit",
                   command=submit)
button.pack()

window.mainloop()
