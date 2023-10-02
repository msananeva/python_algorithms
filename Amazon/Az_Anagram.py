"""
Check whether two strings are anagram of each other
"""
s1 = "Hello "
s2 = "lloeh"

def anagram(s1, s2):
    #  remove spaces at the beginning and at the end of the string
    x = s1.strip().lower()
    y = s2.strip().lower()
    if sorted(x) == sorted(y):
        return True
    else:
        return False

print(anagram(s1, s2))
