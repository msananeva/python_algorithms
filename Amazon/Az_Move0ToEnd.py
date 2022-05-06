nums = [0, 1, 0, 3, 12]
append_times = nums.count(0)
print(append_times)

def moveZeroes(x):
    for i in range(append_times):
        x.remove(0)  # Delete the front zero
        x.append(0)  # Append it at the end of nums
    return x

print(moveZeroes(nums))
