"""
Make a decorator that changes the type of a value sent.
"""

def type_changer(*types):  # args convetion broken intetionally
    
    def intermediary(function):
        
        def conversor(*args, **kwargs):
            new_args = []
            for value, the_type in zip(args, types):
                new_args.append(the_type(value))
            return function(*new_args, **kwargs)
        
        return conversor
    
    return intermediary


@type_changer(str, int)
def repeater(string, times):
    for _ in range(times):
        print(string)


repeater('hehe', '3')
