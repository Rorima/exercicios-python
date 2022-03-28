"""
Use a function as an argument in another function
"""


def discount(price):
    
    new_price = price * 0.8  # 20% discount
    
    def installments(installment_number):
        return new_price / installment_number
        
    return installments


discounted = discount(1200)
print(discounted(10))
