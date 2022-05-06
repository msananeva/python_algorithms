""" Given Aaabbbcc, return a3b3c2 """

input = "Aaabbbcc".lower()

def addNumsToStr(x):
    result = ""
    count = 1
    for char in x:
        if char in result:
            count += 1
        else:
            result += char
            result += str(count)
            count = 1

    return result


print(addNumsToStr(input))
