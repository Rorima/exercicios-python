import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()

# Lines
# canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
# canvas.create_line(0, 500, 500, 0, fill="red", width=5)

# Rectangle
# canvas.create_rectangle(100, 400, 400, 100, fill="purple")

# Polygon
# coordinates = [250, 0, 500, 500, 0, 500]
# canvas.create_polygon(coordinates, fill="yellow", outline="black", width=5)

# Arch
# canvas.create_arc(0, 0, 500, 500, width=3, fill="green", start=90, extent=359)
canvas.create_arc(0, 0, 500, 500, fill="red", extent=180, width=5)
canvas.create_arc(0, 0, 500, 500, fill="white", start=180, extent=180, width=5)
canvas.create_line(0, 250, 500, 250, fill="black", width=30)
canvas.create_oval(190, 190, 310, 310, fill="black")
canvas.create_oval(210, 210, 290, 290, fill="white")


root.mainloop()
