""" Sum of digits in the number """

input = 2022

def sumOfDigits(x):
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum

print(sumOfDigits(input))
