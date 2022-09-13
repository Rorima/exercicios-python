import tkinter as tk
import time

WIDTH = 500
HEIGHT = 500
xvelocity = 2
yvelocity = 3

root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Remember to change path
background_photo = tk.PhotoImage(file="space.png")
space = canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Remember to change path
photo_image = tk.PhotoImage(file="alien.png")
alien = canvas.create_image(0, 0, image=photo_image, anchor="nw")

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(alien)
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        xvelocity = -xvelocity

    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        yvelocity = -yvelocity
    
    canvas.move(alien, xvelocity, yvelocity)
    root.update()
    time.sleep(0.01)

root.mainloop()
