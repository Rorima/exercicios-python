"""
Show only the first two digits after the floating point.
"""
from math import sqrt


def square_root(number):
    result = sqrt(number) 
    return f'{result:.2f}'


print(square_root(12))
print(square_root(13))
print(square_root(14))
print(square_root(15))
