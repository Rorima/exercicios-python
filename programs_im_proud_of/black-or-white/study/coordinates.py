"""
Write an algorithm that creates the coordinates of a chess board.

They go from a to h and from 1 to 8.
a ~ h = horizontal
1 ~ 8 = vertical
"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8)
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')


# I believe this is the best layout to add colors in the future
a = [(f'a{num}') for num in numbers]
b = [(f'b{num}') for num in numbers]
c = [(f'c{num}') for num in numbers]
d = [(f'd{num}') for num in numbers]
e = [(f'e{num}') for num in numbers]
f = [(f'f{num}') for num in numbers]
g = [(f'g{num}') for num in numbers]
h = [(f'h{num}') for num in numbers]

coord_tuple = (a, b, c, d, e, f, g, h)
coordinates = list()

for l in coord_tuple:
    for ln in l:
        coordinates.append(ln)

print(coordinates)
