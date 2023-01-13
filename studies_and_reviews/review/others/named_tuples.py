"""
Named Tuples:

A named tuple is kind of a light weight object that works just like a 
regular tuple but is just more readable.

Let's say we want to represent RGB values using a tuple:
```
color = (55, 155, 255)
```

This is not a very good method because it's not very descriptive.
You might come back to this code sometime later and not know what
it is all about. You could also use a dictionary to make it more
readable:
```
color = {"red": 55, "green": 155, "blue": 255}
```

Dictionaries are mutable and require a little bit more typing. A
namedtuple is a good compromise between a tuple and a dictionary.

If you're going to use a namedtuple, you'll first need to import it:
```
from collections import namedtuple
```

This is the syntax to create a namedtuple:
```
Name = namedtuple("Name", ["value", "value", "value"])
```

This is a named tuple for the RGB values:
```
Color = namedtuple("Color", ["red", "green", "blue"])
```

This is how you add values to the namedtuple:
```
color = Color(red=55, green=155, blue=255)
```

You can print the values in two ways:
```
print(color.red)
print(color[1])
```
"""
from collections import namedtuple

Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(red=55, green=155, blue=255)
white = Color(255, 255, 255)

print(color.red)
