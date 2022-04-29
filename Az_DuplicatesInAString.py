""" Find all duplicate characters in string """

str = "Aaaaaabccccd11"

def allDuplicates(x):
    duplicates = {}
    for i in str:
        if i in duplicates:
            duplicates[i] += 1
        else:
            duplicates[i] = 1

    for key, value in duplicates.items():
        if value > 1:
            print(key, end=" ")

    return duplicates

allDuplicates(str)
