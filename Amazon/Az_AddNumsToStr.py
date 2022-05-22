"""
Given Aaabbbcc, return 3a3b2c
https://www.youtube.com/watch?v=mjZpZ_wcYFg
"""
input = "aaabbbcc"


def addNumsToStr(x):
    result = []

    prevChar = ""
    count = 0

    # iterate over input
    for char in x:
        if char == prevChar:
            count += 1
        else:
            if prevChar != "":  # skip first char
                result.append(count)
                result.append(prevChar)
            prevChar = char
            count = 1
    result.append(count)  # add last char and count
    result.append(prevChar)
    return result

print(addNumsToStr(input))
