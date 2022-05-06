""" Length of the last word """

str = "Hi World"


def lenOfLastWord(x):

    s = (str.split())
    return len(s[-1])

print(lenOfLastWord(str))
