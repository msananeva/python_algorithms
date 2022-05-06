"""
Find number of instances of ‘a’ in string
"""

input = "Hello this is an awesome string".lower()

k = "a"

def occurOfChar(x):
    count = 0
    for char in input:
        if char == k:
            count += 1
    return count

print(occurOfChar(input))
