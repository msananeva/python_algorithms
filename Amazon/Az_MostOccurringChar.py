input = "Aaaaabbbbbcc".lower()

# edge case - spaces

def mostOcurringChar(input):
    all_freq = {}

    input_no_spaces = "".join(input.split())

    for char in input_no_spaces:
        if char in all_freq:
            all_freq[char] += 1
        else:
            all_freq[char] = 1
    return max(all_freq, key=all_freq.get)

print("Most occurring char: ", mostOcurringChar(input))

#________________________________________________________________

# from collections import Counter
#
# str = "AAAAAaaaBbbbcdddDDDdddd".lower()
#
# result = Counter(str)
# result = max(result, key=result.get)
#
# print("Most frequent character: ", result)
