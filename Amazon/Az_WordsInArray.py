""" In an array of names, return the names show up > 1 """

input = ["Mila", "Maxim", "Mila", "Sandy", "Sandy", ""]


def dups(x):
    arr = []
    for el in x:
        c = x.count(el)
        if c > 1 and el not in arr:
            arr.append(el)
    return arr
print(dups(input))
