""" Generate the lower case English letters """

import string


def letters():
    for char in string.ascii_lowercase:
        yield char


for letter in letters():
    print(letter)

#__________________________________________________
    def g():
        yield 1
        yield 2
        yield 3

    print(g())

    for x in g():
        print(x)
