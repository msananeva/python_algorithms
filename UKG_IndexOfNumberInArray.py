""" Position of a number in an array """

a = [1, 23, 9, 5, 7, 9]
num = 9

print(a.index(num))

def positionInArr(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == num:
            result.append(i)
    return result

answer = positionInArr(a)
print(answer)

str2 = []
for el in answer:
    str2.append(str(el))

result = " ".join(str2)
print(result)



