input = "Aaaaabbbbbcc".lower()

def mostOcurringChar(x):
    all_freq = {}
    for i in input:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return max(all_freq, key=all_freq.get)

print("Most occurring char: ", mostOcurringChar(input))

#________________________________________________________________

from collections import Counter

str = "AAAAAaaaBbbbcdddDDDdddd".lower()

result = Counter(str)
result = max(result, key=result.get)

print("Most frequent character: ", result)
