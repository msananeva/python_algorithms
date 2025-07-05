"""
Given an array of integers,
sort the contents into 2 output arrays
where one has all odd numbers and the other has all even numbers
"""

input = [1, 0, 15, 2, 22, 22, 3, 4]

# duplicates?
# 0 is even or odd? Let agree it's none of those

def odd_vs_even(nums):
    odd = []
    even = []
    for num in nums:
        if num == 0:
            continue
        elif num % 2 == 0 and num not in even:
            even.append(num)
        elif num % 2 != 0 and num not in odd:
            odd.append(num)
    return f"Odd nums are: {odd}, Even nums are: {even}"

print(odd_vs_even(input))