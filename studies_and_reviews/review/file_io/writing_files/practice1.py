"""
Create a file and write a couple of lines in it.
"""

lines = ["This will be a test.",
         "Hopefully everything turns out just fine.",
         "OK, let's see what happened..."]

with open("testfile.txt", 'w') as f:
    f.write("\n".join(lines))
    f.write("\n")
