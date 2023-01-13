"""
Closures:

Wikipedia says, "A closure is a record storing a function together
with an environment: a mapping associating each free variable of
the function with the value or storage location to which the name
was bound when the closure was created. A closure, unlike a plain
function, allows the function to access those captured variables
through the closure's reference to them, even when the function is
invoked outside their scope."

Summed up in human language:
A closure closes over the free variables from their environment. In
the case below "message" would be that free variable.
"""


def outer_func(msg):
    message = msg
    
    def inner_func():
        print(message)
    
    return inner_func


hi_func = outer_func("Hi")
hi_func()

hello_func = outer_func("Hello")
hello_func()
