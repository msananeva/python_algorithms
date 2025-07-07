""" In an array of names, return the names show up > 1 """

input = ["Mila", "Maxim", "Mila", "Sandy", "Sandy", ""]


def dups(x):
    result = []
    for name in x:
        occur = x.count(name)
        if occur > 1 and name not in result:
            result.append(name)
    return result
print(dups(input))
