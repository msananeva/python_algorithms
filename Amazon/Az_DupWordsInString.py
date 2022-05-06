""" Return the duplicated words in a string """

input = "Sandy is the best dog. We love Sandy so much!"

def dupWordsInString(x):
    str_to_arr = x.split()
    result = []
    for word in str_to_arr:
        occur = str_to_arr.count(word)
        if occur > 1 and word not in result:
            result.append(word)
    return result

print(dupWordsInString(input))
