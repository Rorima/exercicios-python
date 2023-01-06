"""
No parameters, no sugar.

"""

def my_decorator(function):
    def wrapper():
        print('I decorated.')
        function()
        print('I decorated again.')
    
    return wrapper


def say_hello():
    print('Hello!')


x = my_decorator(say_hello)
x()
