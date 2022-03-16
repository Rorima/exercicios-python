"""
Parameters and syntactic sugar.

"""

def dec(func):
    def wrapper(*args, **kwargs):
        print('Top decoration')
        rv = func(*args, **kwargs)
        print('Bottom decoration')
        return rv
        
    return wrapper


@dec
def sum_it(a, b):
    return(a + b)


x = sum_it(10, 5)
print(x)
