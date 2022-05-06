""" Given an array of numbers return all pairs """

input = [1, 1, 0, 4, -5]
length = len(input)

def allPairs(x):
    pairs = []
    for i in range(length):
        for j in range(length):
            tuple = (x[i],x[j])
            if tuple not in pairs:
                pairs.append(tuple)

    return pairs


print(allPairs(input))

