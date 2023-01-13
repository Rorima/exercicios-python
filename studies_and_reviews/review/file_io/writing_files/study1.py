"""
Steps for writing to text files:

- First, open the text file for writing (or appending) using the open() function.

- Second, write to the text file using the write() or
writelines() method.

- Third, close the file using the close() method.

Sintax:
```
f = open(path_to_file, mode)
```

For writing to a text file, you use one of the following modes:
'w': open a text file for writing text;
'a': open a text file for appending text;



*
Writing text files:

The open() function returns a file object. The file object has two
useful methods for writing text to it: write() and writelines().

The write() method writes a string to a text file, and the
writelines() method writes a list of strings to a file at once.

To write a line to a text file, you need to manually add a new
line character:

```
f.write('\n')
f.writelines('\n')
```
"""
sentences = ["This is just a test", "And this should be the second line", "And this, the third"]

with open("readme.txt", 'w') as f:
    f.write("\n".join(sentences))
