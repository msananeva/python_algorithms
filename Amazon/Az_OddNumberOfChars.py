"""
Write a function that finds the characters in array that appear an odd number of times
"""

input = ["a", "b", "c", "d", "a"]

# do we want to include duplicates? if not, then we can use a set

def occurOddNum(x):
    result = []
    for char in x:
        occur = x.count(char)
        if occur % 2 > 0 and char not in result:
            result.append(char)

    return result

print(occurOddNum(input))
