"""
Given an integer,
find the sum of digits of that number
until the sum becomes a single digit
"""

input = 987

def sumOfDigits(x):
    to_string = str(x)
    sum = 0
    for d in to_string:
        sum += int(d)

        if sum > 9:
            sum = sumOfDigits(sum)

    return sum

print(sumOfDigits(input))
