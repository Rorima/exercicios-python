"""
# Closure
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()
"""

def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}.')
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print('display function ran')


display()
