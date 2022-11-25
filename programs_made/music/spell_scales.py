"""
Purpose: A program to help you learn how to spell scales.

Create a program where the user is trained in the spelling
of a scale. There should appear a scale degree on the screen,
and the user has to answer correctly what is the name of
that note. The user can also choose a mode where the opposite
is presented: a note is shown, and the user has to tell what
is the scale degree.
"""
from random import randint


def treat_input(min_num, max_num):
    """
    Receive the input, treat it and return it cast to int.
    Let the user choose only numbers. The number chosen cannot
    be greater than nor lesser than the number of scales available.
    
    Arguments:
    min_num: The minimun number that the user is allowed to send
    max_num: The maximum number that the user is allowed to send
    """
    
    while True:
        user = input()
        if not user.isdigit():
            print("You have to choose a number.")
            continue
        else:
            if int(user) < min_num or int(user) > max_num:
                print("You have to choose a valid number.")
                continue
        break

    return int(user)


cmajor = ('C Major', 'C', 'D', 'E', 'F', 'G', 'A', 'B')
gmajor = ('G Major', 'G', 'A', 'B', 'C', 'D', 'E', 'F#')
dmajor = ('D Major', 'D', 'E', 'F#', 'G', 'A', 'B', 'C#')
amajor = ('A Major', 'A', 'B', 'C#', 'D', 'E', 'F#', 'G#')
emajor = ('E Major', 'E', 'F#', 'G#', 'A', 'B', 'C#', 'D#')
bmajor = ('B Major', 'B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#')
fshmajor = ('F# Major', 'F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#')
cshmajor = ('C# Major', 'C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#')
fmajor = ('F Major', 'F', 'G', 'A', 'Bb', 'C', 'D', 'E')
bbmajor = ('Bb Major', 'Bb', 'C', 'D', 'Eb', 'F', 'G', 'A')
ebmajor = ('Eb Major', 'Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D')
abmajor = ('Ab Major', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G')
dbmajor = ('Db Major', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C')
gbmajor = ('Gb Major', 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F')
cbmajor = ('Cb Major', 'Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb')

scales = (
    cmajor, gmajor, dmajor, amajor, emajor,
    bmajor, fshmajor, cshmajor, fmajor, bbmajor,
    ebmajor, abmajor, dbmajor, gbmajor, cbmajor
)

for n, s in enumerate(scales, 1): print(n, s[0])

print("What scale do you want to learn how to spell? ")
scale = treat_input(1, 15)

print()
print("In what mode do you want to learn?")
print("1. Read note and type scale degree;")
print("2. Read scale degree and type note;")
mode = treat_input(1, 2)

chosen_scale = scales[scale - 1]

print("Type 'quit' to exit the program.")

previous = None

while True:
    print()
    num = randint(1, 7)
    
    while previous == num:
        num = randint(1, 7)
    
    if mode == 1:
        print("Type the scale degree: ")
        print(chosen_scale[num])
        answer = input()
        
        previous = num
        
        if answer == "quit":
            break
        
        if answer == str(num):
            print("You got it!")
        else:
            print(f"The right answer would be {num}.")
    else:
        print("Type the name of the note: ")
        print(num)
        answer = input().lower()
        
        previous = num
        
        if answer == "quit":
            break
        
        if answer == chosen_scale[num].lower():
            print("You got it!")
        else:
            print(f"The right answer would be {chosen_scale[num]}.")
