"""
Steps for reading a text file in Python:

- First, open a text file for reading by using the open() function.
  
- Second, read text from the text file using the file read(),
readline(), or readlines() method of the file object.
  
- Third, close the file using the file close() method.


*
1) open() function:

open(path_to_file, mode)

If the file is in the same folder as the program, you just need
to specify the name of the file. Otherwise, you need to specify
the path to the file.

To specify the path to the file, you use the foward-slash ('/') even
if you're working in Windows.

The mode is an optional parameter. It's a string that specifies
the mode in which you want to open the file.

Modes and descriptions:
'r' Open a text file for reading text
'w' Open a text file for writing text
'a' Open a text file for appending text

Example:
```
f = open("the-zen-of-python.txt", 'r')
```

The open() function returns an iterable file object which you will 
use to read text from a text file.



2) Reading text methods:

- read() - read all text from a file into a string. This method is
useful if you have a small file and you want to manipulate the whole
text of that file.

- readline() - read the text file line by line and return all the
lines as strings.

- readlines() - read all the lines of the text file and return them
as list of strings.



3) close() method:

The file must be closed, otherwise the program may crash or the
file might get corrupted.

Closing a file:

```
f.close()
```

To close the file automatically without calling the close()
method, you use the with statement:

```
with opne(path_to_file) as f:
    contents = f.readlines()
```

In practice, you'll use the with statement to close the file
automatically.
"""

with open("notes.txt") as f:
    first_line = f.readline()
    print(first_line)

file = open("notes.txt", 'r')
print(file.readline())
file.close()
    
