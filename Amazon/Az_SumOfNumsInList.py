"""
Find the two numbers that add to the passed in sum. Input: list and a sum
"""

input = [1, 10, 9, 4]
k = 5

def sum(x,k):
    for i in x:
        for j in x:
            if i+j == k:
                return i,j

print(sum(input,k))

def ind(x,k):
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i] + x[j] == k:
                return [i, j]

print(ind(input,k))

