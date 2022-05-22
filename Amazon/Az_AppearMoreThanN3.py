""" Given an integer array of size n,
find all elements that appear more than ⌊ n/3 ⌋  """

arr = [1, 5, 7, 15, 7, 7]

def appear3times(x, n):
    n = len(x)
    print(n)
    all_freq = {}
    for d in x:
        if d not in all_freq:
            all_freq[d] = 1
        else:
            all_freq[d] += 1

    for i in all_freq:
        if all_freq[i] > int(n / 3):
            return i


print(appear3times(arr, 6))