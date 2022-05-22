""" Given an array of n length containing number 1 to 99 .
print last 2 digits of result
after multiplying all the n numbers in array.
 """

input = [1, 15, 3, 7, 17]

def lastDigits(x):
    mult = 1
    for d in x:
        mult *= d

    result = mult % 100  # OR
    # return str(mult[-2:])

    return result

print(lastDigits(input))