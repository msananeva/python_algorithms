""" Return the number of vowels in a given sentence """

input = "This is An awesome string!".lower()

def numOfVowels(x):
    all_vowels = "aeiouy"
    vowels_in_string = []
    for char in x:
        if char in all_vowels:
            vowels_in_string.append(char)
    return len(vowels_in_string)


print(numOfVowels(input))

#______________________________________________

def numberOfVowels(x):
    all_vowels = "aeiouy"
    count = 0
    for char in x:
        if char in all_vowels:
            count += 1
    return count

print(numberOfVowels(input))
