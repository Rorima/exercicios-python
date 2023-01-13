"""
# Normal for loop
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sub_list in my_list:
    for number in sub_list:
        print(number)


# List comprehension
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numbers = [number for sub_list in my_list for number in sub_list]
for i in numbers: print(i)


# Maybe not a good practice
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[print(number) for sub_list in my_list for number in sub_list]

"""
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[print(number) for sub_list in my_list for number in sub_list]
