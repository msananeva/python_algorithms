""" Generate the lower case English letters """

import string


def letters():
    for char in string.ascii_lowercase:
        yield char


for letter in letters():
    print(letter)
