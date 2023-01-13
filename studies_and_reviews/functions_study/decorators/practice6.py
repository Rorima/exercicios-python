"""
Write a decorator that takes one parameter.
"""

def decorator(value):
    print('Decorator')
    
    def inner(func):
        print('Inner')
        print(value)
        
        def other():
            return func()
        
        return other()
    
    return inner


@decorator('Well...')
def test():
    print('It worked!')

