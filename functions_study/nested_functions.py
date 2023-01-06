from random import choice

# Nested Functions
def greetings(person):
    def humour():
        return choice(('How is it going, {}?', 'Get away from me, {}!', 'I like you a lot, {}!'))
    return humour().format(person)


# Testing
print(greetings('Angelina'))
print(greetings('Felicity'))
