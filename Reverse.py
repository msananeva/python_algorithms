
arr = [8, 2, 0, 1, 9]
length = len(arr)
lastIndex = length - 1
result = [0] * length  # Initiate an empty array

for i in range(length):
    el = arr[i]
    insertIndex = lastIndex - i
    result[insertIndex] = el

print(result)
