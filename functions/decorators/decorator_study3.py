def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
        
    return wrapper


def func2():
    print("I'm func2")


def func3():
    print("I'm func3")


x = func(func3)
y = func(func2)
x()
y()
