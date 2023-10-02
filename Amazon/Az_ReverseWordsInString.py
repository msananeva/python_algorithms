"""
Write a function that will take a string as input and return a string
that reverses each word from the input.
"""

input = "This is an awesome string"

def reversedWords(x):
    rev = " ".join(reversed(x.split())) #  string awesome an is This
    revWords = rev[::-1] #  gnirts emosewa na si sihT
    return revWords

print(reversedWords(input))
