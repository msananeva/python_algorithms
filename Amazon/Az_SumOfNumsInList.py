"""
Find the two numbers that add to the passed in sum. Input: list and a sum
"""

input = [3, 2, 10, 9, 4]
k = 6


# if I need indexes

def sum(x,k):
    l = len(x)
    for i in range(l):
        for j in range(i+1, l):
            if x[i] + x[j] == k:
                return x[i], x[j]

print(sum(input,k))

