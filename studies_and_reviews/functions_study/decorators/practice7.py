"""
Use a decorator that adds "Thank you!" to the end of
a string.
"""

def decorator(func):
    def thank(*args, **kwargs):
        return func(*args, **kwargs) + ' Thank you!'
    return thank


@decorator
def order(food):
    return f'I would like some {food}, please!'


print(order('rice, beans and salad'))
print(order('water'))
print(order('buttery biscuits'))
