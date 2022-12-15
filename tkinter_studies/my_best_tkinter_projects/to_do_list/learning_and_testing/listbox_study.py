"""
"""
from tkinter import *


def delete():
    """Delete the anchor object
    
    The anchor is not the selected object per se,
    but it's almost.
    """
    my_listbox.delete("anchor")
    my_label.config(text='')


def select():
    """Select the anchor object"""
    my_label.config(text=my_listbox.get("anchor"))


def delete_all():
    """Delete all items from index 0 to the last index"""
    my_listbox.delete(0, "end")
    my_label.config(text='')


def select_all():
    """Select all items at once
    
    The curselection method returns the index of the selected
    item. The get method returns the item when given the
    index. When several items are selected, we can get one
    by one by using a for loop.
    """
    result = ''

    for item in my_listbox.curselection():
        result = result + str(my_listbox.get(item)) + '\n'

    my_label.config(text=result)


def delete_multiple():
    """Delete selected items
    
    This function works almost the same way the previous function.
    The main difference is that the reversed function is used. It's
    used because if you try to delete an item from the top of the list,
    it will get messed up and you wont be able to delete the expected
    items after the one that you deleted, so you have to delete them
    from the bottom to the top. Using the reverse method, you can do
    that.
    """
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)


# Creating the window
root = Tk()
root.geometry("400x400")

# Creating a frame to hold the scrollbar
frame = Frame(root)

# Creating the scrollbar and fixing it on the frame
scrollbar = Scrollbar(frame, orient="vertical")

# Creating the listbox and fixing it to the frame.
# Telling that the bar will be vertical. The
# extended mode enables to select several items
# with ctrl or shift.
my_listbox = Listbox(frame, height=5, yscrollcommand=scrollbar.set, selectmode="extended")

# Configuring the scroll bar to be vertical and be attatched
# to my_listbox
scrollbar.config(command=my_listbox.yview)

# Packing the scrollbar and making it fill the whole y space.
scrollbar.pack(side="right", fill="y")
frame.pack()
my_listbox.pack(pady=15)

# Inserting items at the end of my_listbox
my_listbox.insert("end", "this is an item")
my_listbox.insert("end", "second item")

# Adding several items to the list of items
my_list = ["one", "two", "three","one", "two", "three","one", "two", "three","one", "two", "three"]
for item in my_list:
    my_listbox.insert("end", item)

delete_button = Button(root, text="delete", command=delete)
delete_button.pack(pady=10)

select_button = Button(root, text="select", command=select)
select_button.pack(pady=10)

delete_all_b = Button(root, text="delete all", command=delete_all)
delete_all_b.pack(pady=10)

select_all_b = Button(root, text="select all", command=select_all)
select_all_b.pack(pady=10)

delete_multiple_b = Button(root, text="delete multiple", command=delete_multiple)
delete_multiple_b.pack(pady=10)

# Label to display selected items
my_label = Label(root, text='')
my_label.pack(pady=5)

root.mainloop()
