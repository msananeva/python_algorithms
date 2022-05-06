input = [1, 0, 5, 0, -1, 10]
length = len(input)

def secondLowerNum(x):
    arr = []
    x.sort()
    for el in x:
        if el not in arr:
            arr.append(el)
    return arr[1]

print(secondLowerNum(input))
#________________________________________________

input_to_set = set(input)

set_to_list = list(input_to_set)

set_to_list.sort()

answer = set_to_list[1]

print(answer)
