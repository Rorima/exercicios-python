"""
Use wraps.
"""
from functools import wraps


def decorator(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function documentation"""
        return func(*args, **kwargs)
    return wrapper


@decorator
def say_hi(msg):
    """say_hi function documentation"""
    return msg

print(say_hi('Hi!'))
print(say_hi.__doc__)
