"""
Write a function that will take a string as input and return a string
that reverses each word from the input.
"""

input = "This is an awesome string"

def reversedWords(x):
    rev = " ".join(reversed(x.split()))
    revWords = rev[::-1]
    return revWords

print(reversedWords(input))
