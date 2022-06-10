"""
First-Class Functions:
"A Programming language is said to have first-class functions if it
treats functions as first-class citizens."

First-Class Citizen (Programming):
"A first-class citizen (sometimes called first-class objects) in a
programming language is an entity which supports all the operations
generally available to other entities. These operations typically
include being passed as an argument, return from a function, and
assigned to a variable."
"""

"""
Assigning a function to a variable:

def square(x):
    return x * x


f = square(5)  # Assigning the result of a function to a variable
f1 = square  # Assigning the function to a variable

print(f)
print(f1(5))

"""

"""
Taking a function as an argument:

square = lambda x: x * x
cube = lambda x: x ** 3

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])

print(squares)
print(cubes)
"""

"""
Returning a function:

This is what we call a closure:

def logger(msg):
    
    def log_message():
        print(f"Log: {msg}")
    
    return log_message


log_hi = logger("Hello, there!")
log_hi()
"""

# A practical use for this:


def html_tag(tag):

    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")
    
    return wrap_text


print_h1 = html_tag('h1')
print_h1("Test Headline!")

print_p = html_tag('p')
print_p("Test Paragraph!")
