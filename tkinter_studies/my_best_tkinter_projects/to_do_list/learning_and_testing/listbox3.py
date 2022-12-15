from tkinter import *


def delete():
    my_listbox.delete("anchor")
    my_label.config(text='')

def select():
    my_label.config(text=my_listbox.get("anchor"))

def delete_all():
    my_listbox.delete(0, "end")
    my_label.config(text='')

def select_all():
    result = ''

    for item in my_listbox.curselection():
        result = result + str(my_listbox.get(item)) + '\n'

    my_label.config(text=result)

def delete_multiple():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)


root = Tk()
root.geometry("400x400")

frame = Frame(root)
scrollbar = Scrollbar(frame, orient="vertical")

my_listbox = Listbox(frame, height=5, yscrollcommand=scrollbar.set, selectmode="extended")

scrollbar.config(command=my_listbox.yview)
scrollbar.pack(side="right", fill="y")
frame.pack()
my_listbox.pack(pady=15)

my_listbox.insert("end", "this is an item")
my_listbox.insert("end", "second item")

# Add list of items
my_list = ["one", "two", "three","one", "two", "three","one", "two", "three","one", "two", "three"]
for item in my_list:
    my_listbox.insert("end", item)

my_button = Button(root, text="delete", command=delete)
my_button.pack(pady=10)

my_button2 = Button(root, text="select", command=select)
my_button2.pack(pady=10)

my_button3 = Button(root, text="delete all", command=delete_all)
my_button3.pack(pady=10)

my_button4 = Button(root, text="select all", command=select_all)
my_button4.pack(pady=10)

my_button5 = Button(root, text="delete multiple", command=delete_multiple)
my_button5.pack(pady=10)

my_label = Label(root, text='')
my_label.pack(pady=5)

root.mainloop()
