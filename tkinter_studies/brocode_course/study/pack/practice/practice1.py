"""
Create 6 different labels. Three should be stacked upon one another
and the last three should be side by side on the bottom.
"""
import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)

label1 = tk.Label(text="Top", bg="red", fg="white")
label1.pack(fill="both", expand=True)

label2 = tk.Label(text="Middle", bg="blue", fg="white")
label2.pack(fill="both", expand=True)

label3 = tk.Label(text="Bottom", bg="green", fg="white")
label3.pack(fill="both", expand=True)

label4 = tk.Label(text="Bottom Left", bg="yellow")
label4.pack(fill="both", expand=True, side="left", ipady=12)

label5 = tk.Label(text="Bottom Center", bg="purple", fg="white")
label5.pack(fill="both", expand=True, side="left", ipady=12)

label6 = tk.Label(text="Bottom Right", bg="orange")
label6.pack(fill="both", expand=True, side="left", ipady=12)

root.mainloop()
