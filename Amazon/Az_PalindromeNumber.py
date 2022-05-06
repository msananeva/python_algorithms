""" Palindrome Number"""

num = 121

str = str(num)
strReversed = "".join(reversed(str))
num2 = int(strReversed)


def isPalindrome(x):
    if x < 0:
        return False
    if num == num2:
        return True
    else:
        return False

print(isPalindrome(num))

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
