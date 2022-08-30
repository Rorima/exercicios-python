"""
Create a window 300x200;
The window's title should be "Shop";
Change the icon for something of your preference;

"""
from tkinter import *

window = Tk()

window.geometry("300x200")
window.title("Shop")

icon = PhotoImage(file='anystuff.png')
window.iconphoto(True, icon)

window.mainloop()
