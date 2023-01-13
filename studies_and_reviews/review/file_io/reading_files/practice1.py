"""
Open a file using the with and not using it, and print the lines
of the file on the terminal. Open a UTF-8 file.
"""

with open("file_io/test.txt") as f:
    for line in f:
        print(line)

f = open("file_io/test.txt")
first_line = f.readline()
f.close()

print(first_line)

japanese_file = open("file_io/japanese.txt", encoding="utf8")
content = japanese_file.read()
japanese_file.close()

print(content)
