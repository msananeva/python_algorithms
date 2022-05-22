"""
Given an array of integers,
sort the contents into 2 output arrays
where one has all odd numbers and the other has all even numbers
"""

input = [1, 0, 15, 2, 22, 22, 3, 4]

# duplicates?
# 0 is even or not odd nor even? Let agree it's non of those

def oddVsEven(x):
    odd = []
    even = []

    for num in x:
        if num == 0:
            pass
        elif num % 2 == 0 and num not in odd:
            odd.append(num)
        else:
            even.append(num)
    return("Odd nums are: ", odd, "Even nums are: ", even)

print(oddVsEven(input))