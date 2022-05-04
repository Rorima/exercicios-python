"""
Make the algorithm to find the smallest
integer in an array.
"""
from random import randint


def find_smallest_integer(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest


lst1 = [randint(-100, 100) for _ in range(10)]
lst2 = [randint(-100, 100) for _ in range(10)]
lst3 = [randint(-100, 100) for _ in range(10)]
lst4 = [randint(-100, 100) for _ in range(10)]
lst5 = [randint(-100, 100) for _ in range(10)]

# Testing with my function and the min function
print(find_smallest_integer(lst1))
print(min(lst1))
print()

print(find_smallest_integer(lst2))
print(min(lst2))
print()

print(find_smallest_integer(lst3))
print(min(lst3))
print()

print(find_smallest_integer(lst4))
print(min(lst4))
print()

print(find_smallest_integer(lst5))
print(min(lst5))
print()
