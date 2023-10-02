"""
Given 2 string arrays,
create a method to return all the common strings in both arrays
"""

input1 = ["This", "is", "an", "Amazing World", "Apricot"]
input2 = ["Apricot", "This", "is", "an", "Amazing", "Test"]

# what if one arr is empty
# what if both are empty
# how about duplicated match
# what if there is no match
# how about partial match

def match(arr1, arr2):
    common_words = []
    for el1 in arr1:
        for el2 in arr2:
            if el2 in arr1:
                common_words.append(el2)
        return common_words

print(match(input1, input2))
