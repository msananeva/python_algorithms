""" Palindrome Number"""

input = 121


def isPalindrome(x):
    if x < 0:
        return False
    # if x < 0:  #convert to positive
    #     x = x * -1 OR x = abs(x)
    to_string = str(x)
    if to_string == to_string[::-1]:
        return True
    else:
        return False

print(isPalindrome(input))

#__________________________________________________

class Solution:

    def isPalindrome(self, x: int) -> bool:

        numToString = str(x)
        reversedNum = "".join(reversed(numToString))

        try:
            num2 = int(reversedNum)
        except:
            return False

        if x == num2:
            return True
        else:
            return False
