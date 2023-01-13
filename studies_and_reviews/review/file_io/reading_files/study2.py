"""
Read UTF-8 text files:

To open a UTF-8 text file, you need to pass the encoding="utf-8" to
the open() function to instruct it to expect UTF-8 characters from
the file.

```
with open("japanese.txt", encoding="utf8") as f:
    for line in f:
        print(line.strip())
```
"""
with open("japanese.txt", encoding="utf8") as f:
    for line in f:
        print(line)
