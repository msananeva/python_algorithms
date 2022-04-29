""" Number of negatives in array """

arr = [0, -1, 7, 10, -3]


def numOfNeg(x):
    num = 0
    for i in arr:
        if i < 0:
            num += 1
    return num

print(numOfNeg(arr))
