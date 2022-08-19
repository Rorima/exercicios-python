"""
Create a new file and use the two methods for writing. Open the
same file and append some text to it.
"""
line = "About love:\n\n"
lines = [
    "Love cannot be bought.\n",
    "Love is not deserved.\n",
    "Love is received.\n\n"
]

love = "I was loved enough to receive life.\n"

with open("text.txt", 'w') as f:
    f.write(line)
    f.writelines(lines)

with open("text.txt", 'a') as f:
    f.write(love)
