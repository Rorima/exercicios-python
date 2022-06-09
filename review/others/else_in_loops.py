"""
The else statement for loops:

In a normal if else code, only one block will be executed, however,
when you have an else after a loop, both blocks can run with no
problems whatsoever. The else after the loop simply means that the
else block will only be executed if the loop is not broken. You
can see the else after a loop as a "no break". It will only execute
if the loop is completed without any breaks.

"""

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    print(i)
else:
    print("Hit the For/Else Statement!")
