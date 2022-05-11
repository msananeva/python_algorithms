""" Reverse an array """

arr = [8, 2, 0, 1, 9]

rev = arr[::-1]
print(rev)

#  OR

def reversed(x):
    new = x[::-1]
    return new

print(reversed(arr))

# length = len(input)
# lastIndex = length - 1
# result = [0] * length  # Initiate an empty array
#
# def rev(x):
#     for i in range(length):
#         el = x[i]
#         insertIndex = lastIndex - i
#         result[insertIndex] = el
#
# print(rev(input))
#
