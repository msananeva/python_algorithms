""" Find all duplicate characters in string """

input = "Aaaaaabccccd11".lower()

#  empty string
#  case insensitive
#  no dups
#  string len == 1

def allDups(x):
    all_freq = {}
    arr = []
    for char in x:
        if char in all_freq:
            all_freq[char] += 1
        else:
            all_freq[char] = 1

    for char in all_freq:
        if all_freq[char] > 1:
            arr.append(char)
    return arr


print(allDups(input))

#_________________________

def allDuplicates(x):
    all_dups = ""
    for char in x:
        freq = x.count(char)
        if freq > 1 and char not in all_dups:
            all_dups += char
    return all_dups

print(allDuplicates(input))