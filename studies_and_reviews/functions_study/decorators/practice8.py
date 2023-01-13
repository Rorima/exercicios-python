"""
Create a decorator that checks if the arguments sent
are equal to the parameters of the decorator.
"""

def decorator(name):
    def inner(func):
        def inside(*args, **kwargs):
            if name != args[0]:
                return f'Incorrect value. The correct value is: {name}.'
            return func(*args, **kwargs)
        return inside
    return inner


@decorator('Coraline')
def name_displayer(*args):
    return args


print(name_displayer('Coraline', 'Wyborne'))
print(name_displayer('Wyborne'))
