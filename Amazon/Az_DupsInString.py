"""
Write a function that takes a single string
and returns the list of duplicate characters

"""

input = "This is an awesome string"

# empty string
# 1 element
# should we include space?
# no duplicates

def dups(x):
    dups = []

    if len(x) == 0:
        return "The string is empty"

    elif len(x) == 1:
        return x[0]

    else:
        for char in x:
            if x.count(char) > 1 and char not in dups:
                dups.append(char)
        return dups

print(dups(input))