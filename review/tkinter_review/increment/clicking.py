import tkinter as tk

total_clicks = 0
clicks = 0
click_price = 5
click_rate = 1


def add_total_clicks():
    global total_clicks
    total_clicks += 1
    total_clicks_label.config(text=total_clicks)


def click():
    global clicks
    add_total_clicks()
    clicks += click_rate
    number_displaying_label.config(text=clicks)


def buy_clicks():
    global clicks, click_price, click_rate
    
    if clicks >= click_price:
        clicks -= click_price
        click_rate += 1
        click_price = round(click_price * 1.2)
        print(click_price)
        
        number_displaying_label.config(text=clicks)
        click_price_label.config(text=click_price)


window = tk.Tk()
window.minsize(width=600, height=400)
window.state("zoomed")


total_clicks_label = tk.Label(
    window,
    font=("Concoslas", 20),
    text=total_clicks
)
total_clicks_label.pack(side="left", anchor="n")


number_displaying_label = tk.Label(
    window,
    font=("Consolas", 40),
    text=0
)
number_displaying_label.pack(pady=100)


buy_clicks_button = tk.Button(
    window,
    text="Buy Clicks",
    font=("Consolas", 20),
    bg="#D0D0D0",
    command=buy_clicks
)
buy_clicks_button.pack(side="bottom", anchor='e')


click_price_label = tk.Label(
    window,
    text=click_price,
    font=("Consolas", 20)
)
click_price_label.pack(side="bottom", anchor='e')


click_button = tk.Button(
    window,
    text="Click Me",
    font=("Consolas", 40),
    bg="#D0D0D0",
    command=click
)
click_button.pack(side="bottom", pady=100, ipady=50)

window.mainloop()
