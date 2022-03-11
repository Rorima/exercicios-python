"""
LEGB
Local, Enclosing, Global, Built-in


# This is a global variable because it's in the main body of our file
x = 'global x'


def test():
    # This is a local variable because it's inside a function
    y = 'local y'
    # print(y)
    
    # You can access variables from the outer scope inside a function
    print(x)


test()

# Outside a function, you cannot access local variables
# print(y)

print(x)



x = 'global x'


def test():
    global x
    x = 'local x'
    print(x)


test()
print(x)



"""
x = 'global x'

def outer():
    x = 'outer x'
    
    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
print(x)
