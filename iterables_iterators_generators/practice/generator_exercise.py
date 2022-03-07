"""
Generator exercise:

Create a program that pair all the possible
combinations for a number and a letter.
"""


def my_generator(letters, numbers):
    """Make tuples with the possible combinations for letters and numbers"""
    for letter in letters:
        for number in numbers:
            yield (letter, number)


letters = ('a', 'b', 'c')
numbers = (1, 2, 3)

# test = ([(letter, number) for number in numbers] for letter in letters)

test = my_generator(letters, numbers)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
