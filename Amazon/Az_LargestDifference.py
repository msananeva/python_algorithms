"""
Given an array S of n integers,
find the pair with the largest difference between
"""

input = [12, 14, 1, 6]

# input = [0,0]
# input = [1,1]
# input = []
# input may include negatives (use abs(d1))
# input may include 2 pairs w the same difference
# do we need to keep pairs in order?
# if there is 0 then return max num and 0

def pairWithLargestDiff(x):
    max_diff = 0
    pair = []
    l = len(x)

    if l == 0 or l == 1:
        print("There is not enough data")

    elif l == 2 and x[0] == x[1]:
        print("There is just 1 pair")

    elif 0 in x:  # doesn't work at all times
        max_num = max(x)
        pair = max_num, 0

    else:
        for i in range(l):
            for j in range(i+1, l):
                diff = x[i] - x[j]
                if diff > 0 and diff > max_diff:
                    pair = x[i], x[j]
    return pair


print(pairWithLargestDiff(input))
