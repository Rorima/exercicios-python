"""
Use the structure "yield from".
"""


def square(iterable):
    squares = []
    for i in iterable:
        squares.append(i*i)
    
    yield from squares


iterable = (1, 2, 3, 4, 5)
test = square(iterable)

for i in test:
    print(i)
