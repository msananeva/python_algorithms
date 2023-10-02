""" Given an array of numbers return all pairs """

input = [1, 1, 0, 4, -5]

def allPairs(x):
    l = len(x)
    pairs = []
    for i in range(l):
        for j in range(l):
            tuple = (x[i],x[j])
            if tuple not in pairs:
                pairs.append(tuple)

    return pairs


print(allPairs(input))

