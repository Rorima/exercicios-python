import tkinter as tk


def order():
    ordered = ['You ordered a pizza!', 'You ordered a hamburger!', 'You ordered a hotdog!']
    print(ordered[x.get()])


food = ["Pizza", "Hamburger", "Hotdog"]

window = tk.Tk()

x = tk.IntVar()

pizza_image = tk.PhotoImage(file='programas\\study\\radiobuttons\\pizza.png')
hamburger_image = tk.PhotoImage(file='programas\\study\\radiobuttons\\hamburger.png')
hotdog_image = tk.PhotoImage(file='programas\\study\\radiobuttons\\hotdog.png')

food_images = [pizza_image, hamburger_image, hotdog_image]

for index in range(len(food)):
    radiobutton = tk.Radiobutton(window, 
                                 text=food[index],
                                 font=("Arial", 20),
                                 variable=x,
                                 value=index,
                                 padx=25,
                                 image=food_images[index],
                                 compound="left",
                                 command=order)
    radiobutton.pack(anchor='w')

window.mainloop()
