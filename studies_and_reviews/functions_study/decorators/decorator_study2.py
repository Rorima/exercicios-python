def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        f(*args, **kwargs)
        print("Ended")
    
    return wrapper


@func
def func2():
    print("I'm func2")


@func
def func3():
    print("I'm func3")


func3()
func2()
