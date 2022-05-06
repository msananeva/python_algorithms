"""
Write a function that finds the characters in array that appear an odd number of times
"""

input = ["a", "b", "c", "d", "a" ]

def occurOddNum(x):
    result = []
    for char in x:
        occur = x.count(char)
        if occur % 2 > 0:
            result.append(char)

    return result

print(occurOddNum(input))
