from tkinter import *

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


root.mainloop()
