"""
From within a function, change a global variable.
"""

total = 0


def adder(number):
    global total
    try:
        total += int(number)
    except (TypeError, ValueError):
        return 'You can only add integers.'
    return total


print('Type a number to be added to the total or type "exit" to exit the program:')

while True:
    
    user = input('|')
    
    if user.isalpha():
        user = user.lower()
        
        if user == 'exit':
            print('You exited the program successfully!')
            break
        else:
            print('Unrecognized command.')
        
    else:
        print(f'Total: {adder(user)}')
