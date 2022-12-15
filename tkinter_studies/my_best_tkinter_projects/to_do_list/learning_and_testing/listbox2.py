from tkinter import *


def delete():
    my_listbox.delete("anchor")
    my_label.config(text='')

def select():
    my_label.config(text=my_listbox.get("anchor"))


root = Tk()
root.geometry("400x400")

my_listbox = Listbox(root)
my_listbox.pack(pady=15)

my_listbox.insert("end", "this is an item")
my_listbox.insert("end", "second item")

# Add list of items
my_list = ["one", "two", "three"]
for item in my_list:
    my_listbox.insert("end", item)

my_button = Button(root, text="delete", command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text="select", command=select)
my_button2.pack(pady=10)

my_label = Label(root, text='')
my_label.pack(pady=5)

root.mainloop()
