nums = [0, 1, 0, 3, 12]

def moveZeroes(x):
    append_times = x.count(0)

    for i in range(append_times):
        x.remove(0)  # Delete the front zero
        x.append(0)  # Append it at the end of nums
    return x

print(moveZeroes(nums))
