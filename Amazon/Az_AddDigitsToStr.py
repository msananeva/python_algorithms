"""
Add digits to the string
Given "Aaaaaabbbbbcc"
Return a1b2c3
"""

input = "Aaaaabbbbbccc".lower()

#  Return a str without dups

def strNoDupsWithDigits(x):
    result = ""
    count = 0
    for char in x:
        if char in result:
            continue
        else:
            result += char
            count += 1
            result += str(count)
    return result

print(strNoDupsWithDigits(input))
