"""

"""
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

main_frame = tk.Frame(root)
main_frame.pack(expand=True)

b1= tk.Button(main_frame, text='1').grid(row=0, column=0)
b2= tk.Button(main_frame, text='2').grid(row=0, column=1, sticky='we')
b3= tk.Button(main_frame, text='3').grid(row=0, column=2)
b4 = tk.Button(main_frame, text="Button").grid(row=1, column=1)

root.mainloop()
