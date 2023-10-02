"""
Given a list of three-digit numbers as input,
write a function that prints the unique combinations of digits
as well as the sum of the digits. (Example: Input: 111 Output: 111:3)
"""
# if needed to return ALL

input = [1, 2, 3]

# empty input
# what if all digits are the same

def shuffleAndSum(x):
    # declare the sum of nums in array
    sum = 0
    result = []
    l = len(x)
    #  using the nested for loop to iterate over element in 3 digit array
    for i in range(l):
        sum += x[i]
        for j in range(l):
            for k in range(l):
                if x[i] != x[j] and x[j]!= x[k] and x[i] != x[k]:
                    tuple = (x[i], x[j], x[k])
                    if tuple not in result and list(tuple) != x:
                        result.append(tuple)
    #  if all digits are the same
    if len(result) == 0:
        result = x

    return result, sum

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
