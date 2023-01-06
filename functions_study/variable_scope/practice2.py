"""
Change a local variable from within a nested function.
"""

def backwards(string):
    
    words = string.split()
    
    def reverser():
        nonlocal words
        words.reverse()
        words = ' '.join(words)
        return words
    
    reverser()
    return words


sentence = ('They say a comic says funny things, but a comedian '
            'says things funny. This makes me a juggler')

print(sentence)
print(backwards(sentence))
