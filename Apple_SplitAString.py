"""
"Creat method called split_string that takes two arguments,
string and character, and it returns a list of substrings that are obtained
from splitting the given string using the character as delimeter "

"""



stri = "PythonPython"
de = "t"
a = []

def split_string(s, d):

    temp = ""
    for i in s:
        if i == d:
            a.append(temp)
            temp = ""
        else:
            temp = temp + i
    return a


print(split_string(stri, de))
