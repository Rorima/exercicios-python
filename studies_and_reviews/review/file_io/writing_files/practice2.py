"""
Append a couple of lines to a file you have already created.
"""
listy = ["This line is for the appending section",
         "This one too!"]

with open("testfile.txt", 'a') as f:
    f.write("\n".join(listy))
    f.write("\n")
