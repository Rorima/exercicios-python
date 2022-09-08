from tkinter import *

window = Tk()  # Instantiate an instance of a window

window.geometry("400x500")
window.title("Learning Program")

icon = PhotoImage(file='myicon.png')  # Turning the png into an icon
window.iconphoto(True, icon)  # Making it the icon of my program

window.mainloop()  # Places window on computer screen, listens for events
