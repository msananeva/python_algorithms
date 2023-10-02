"""
Given Aaabbbcc, return 3a3b2c
https://www.youtube.com/watch?v=mjZpZ_wcYFg
"""
input = "aaabbbcc"

# empty string
# case sensitive?

def addNumsToStr(x):
    if x == "" or len(x) == 0:
        return ""

    # declare the previous character variable
    prevChar = ""
    count = 0
    result = ""
    for char in x:
        if char == prevChar:
            count += 1
        elif prevChar == "":  # skip first char
            prevChar = char
            count = 1
        else:
            result += str(count)
            result += char
            prevChar = char
            count = 1
    result += str(count)  # add last char and count
    result += char
    return result

print(addNumsToStr(input))
