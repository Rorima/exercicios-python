"""
Let's say we want to create a sentence object where
we expect a string of words, and when we loop over the
sentence, we simply loop over the words in the sentence.

Do it first with a class, and then with a generator.
"""


def sentence(sentc):
    yield from sentc.split()


my_sentence = sentence('This is a test')

for word in my_sentence:
    print(word)

# Expected result:
# This
# is
# a
# test
