""" Return the duplicated words in a string """

input = "Sandy is the best dog. We love Sandy so much!"

# no dup words
# upper case lower case matter?
# do we want to count a 1 char word as word?
# empty string

def dups(input):
    x = input.split()
    result = []
    for word in x:
        if x.count(word) > 1 and word not in result:
            result.append(word)
            return result
        else:
            return "No duplicates"


print(dups(input))
