""" Palindrome String """

str = "Abba".lower()

def isPalindrome(x):
    if str == str[::-1]:
        return True
    else:
        return False

print(isPalindrome(str))
