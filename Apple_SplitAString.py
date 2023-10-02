"""
"Creat method called split_string that takes two arguments,
string and character, and it returns a list of substrings that are obtained
from splitting the given string using the character as delimeter "

"""



input = "PythonPython"
de = "t"


def split_string(x, d):
    result = []
    temp = ""
    for char in x:
        if char == d:
            result.append(temp)
            temp = ""
        else:
            temp = temp + char
    result.append(temp)
    return result


print(split_string(input, de))
