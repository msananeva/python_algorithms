""" Longest Palindrome in a String """

input = "Alola mem test aaaaaaaa KKKakkk".lower().split()

def longestPalindrome(x):
    arr = []
    for el in x:
        if str(el) == str(el)[::-1]:
            arr.append(el)
    return max(arr, key=len)

print(longestPalindrome(input))