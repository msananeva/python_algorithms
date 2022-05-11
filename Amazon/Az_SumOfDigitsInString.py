""" Sum of digits in the given string """

input = "This is a string with digits 1 and 15"

def sumOfDigits(x):
    sum = 0
    arr = x.split()
    for el in arr:
        if el.isdigit():
            sum += int(el)
    return sum
print(sumOfDigits(input))
