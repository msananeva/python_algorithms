"""
Given a list of three-digit numbers as input,
write a function that prints the unique combinations of digits
as well as the sum of the digits. (Example: Input: 111 Output: 111:3)
"""
# if needed to return ALL

input = [1, 2, 3]
l = len(input)

def shuffleAndSum(x):
    arr = []
    s = 0
    for i in range(l):
        for j in range(l):
            for k in range(l):
                if x[i] != x[j] and x[j] != x[k] and x[i] != x[k]:
                    tuple = (x[i], x[j], x[k])
                    if tuple not in arr:
                        arr.append(tuple)

    for i in range(l):
        s += x[i]

    return arr, s

print(shuffleAndSum(input))





import random
from random import randint

# input = [5, 7, 1]
#
# l = len(input)
#
# def shuffleAndSum(x):
#     for i in range(l-1, 0, l):
#         j = randint(0, i + 1)
#         x[i], x[j] = x[j], x[i]
#         return x
#
#     s = 0
#     for i in range(l):
#         s += x[i]
#     return x, s
#
# print(shuffleAndSum(input))
