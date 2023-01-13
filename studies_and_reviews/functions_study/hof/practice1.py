def capitalizing(string):
    return string.capitalize()


def fixer(func, lst):
    fixed = []
    for string in lst:
        fixed.append(func(string))
    return fixed


a_list = ["hello, my wonderful friends!", "i'm so happy! aha! Happy go lucky me!", "things that bother you never bother me."]
print(fixer(capitalizing, a_list))
