input = "2 7 11 15".split()
target = int("9")

# def convertToInt(x):
#     try:
#         number = int(x)
#     except:
#         print("Oh oh")
#         exit(1)
#
# mapped = map(convertToInt, input)
# nums = list(mapped)
nums = [int(el) for el in input]

length = len(nums)

def twosum(x):
    for i in range(length):
        for j in range(i+1, length):
            if nums[j] == target - nums[i]:
                return [i, j]

el = twosum(target)

print(el)
