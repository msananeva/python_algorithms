""" Most occurring num  """

input = [1, 0, 1, 15, 55, 1, 555]

def mostFreqNum(arr):
    max_freq = 0
    answer = 0
    for d in arr:
        count = arr.count(d)
        if count > max_freq:
            max_freq = count
            answer = d
    return answer


print(mostFreqNum(input))