"""
Let's say we want to create a sentence object where
we expect a string of words, and when we loop over the
sentence, we simply loop over the words in the sentence.

Do it first with a class, and then with a generator.

"""


class Sentence:
    dummy = 0
    
    def __init__(self, string):
        self.string = string
        self.splitted = self.string.split()
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        index = self.dummy
        if self.dummy == len(self.splitted):
            raise StopIteration
        
        self.dummy += 1
        return self.splitted[index]


my_sentence = Sentence('This is a test')


for word in my_sentence:
    print(word)

# Expected result:
# This
# is
# a
# test
