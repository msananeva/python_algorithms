"""
Check whether two strings are anagram of each other
"""
s1 = "Hello "
s2 = "lloeh"

def anagram(s1, s2):
    if sorted(s1.strip().lower()) == sorted(s2.strip().lower()):
        return True
    else:
        return False

print(anagram(s1, s2))
