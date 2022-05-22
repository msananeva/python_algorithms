"""
Write a function that takes a single string
and returns the list of duplicate characters

"""

input = "This is an awesome string"

# empty string
# 1 element
# should we include space?
# no duplicates

def dupEl(x):
    all_freq = []

    if len(x) == 0:
        return "The string is empty"

    elif len(x) == 1:
        return x[0]

    else:
        for el in x:
            if x.count(el) > 1 and el not in all_freq:
                all_freq.append(el)
                return all_freq
            else:
                return "There are no dups"

print(dupEl(input))