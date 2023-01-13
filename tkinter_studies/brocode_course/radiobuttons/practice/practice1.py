"""
Create a program that asks the user for the name and the class of their character.
"""
import tkinter as tk


def greetings():
    name = user_name.get()
    print(f"Hello, {name}. Welcome to the battle!")


def chosen_class():
    chosen = ["You chose warrior.", "You chose ranger.", "You chose berserker."]
    print(chosen[x.get()])


classes = ["Warrior", "Ranger", "Berserker"]

window = tk.Tk()

window.title('RPG')

message = tk.Label(window, text='Write the name of your character:', font=('Calibri', 20))
user_name = tk.Entry(window, font=('Calibri', 25))
submit_button = tk.Button(window, text='Submit', font=('Calibri', 20), command=greetings)

message.grid()
user_name.grid(row=1, sticky='w')
submit_button.grid(row=1, column=1, sticky='w')

message2 = tk.Label(window, text='Choose your class:', font=('Calibri', 20))
message2.grid()

x = tk.IntVar()

for index in range(len(classes)):
    class_button = tk.Radiobutton(window,
                                  text=classes[index],
                                  variable=x,
                                  value=index,
                                  command=chosen_class)
    class_button.grid(sticky='w')

window.mainloop()
