"""
Write a program using class methods.
"""
"""
The more products added to the class, the higher the discount.
"""


class GoodDiscount:

    product_amt = 0
    total_discount = 1.0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        GoodDiscount.product_amt += 1
        GoodDiscount.raise_total_discount()

    def apply_discount(self):
        self.price = self.price * GoodDiscount.total_discount

    @classmethod
    def raise_total_discount(cls):
        cls.total_discount += 0.01


product1 = GoodDiscount('PlayHouse 5', 30)
product2 = GoodDiscount('Zbox 180', 20)
product3 = GoodDiscount('Mini Tendo Swift', 20)

product3.apply_discount()
print(product3.price)
