""" Longest Palindrome in a String """

input = "Alola mem test aaaaaa KKKakkk"

def longestPalindrome(x):
    string_to_lower = x.lower()
    str_to_arr = string_to_lower.split()
    arr = []
    for word in str_to_arr:
        if str(word) == str(word)[::-1]:
            arr.append(word)
    return max(arr, key=len)

print(longestPalindrome(input))