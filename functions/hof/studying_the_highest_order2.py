"""
# First example: accpeting a function as an argument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func('Hello')
    print(text)


hello(loud)
hello(quiet)
"""


# Second example: returning a function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))
