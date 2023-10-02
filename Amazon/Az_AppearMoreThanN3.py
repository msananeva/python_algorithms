""" Given an integer array of size n,
find all elements that appear more than ⌊ n/3 ⌋  """

arr = [1, 5, 7, 15, 7, 7]

# no more
# a couple of results
# empty array

def appear4PlusTimes(x):
    l = len(x)
    #  declare the target count variable
    target_count = l/3
    #  initiating an empty array to store nums that appear more than l/3 times
    result = []
    for d in x:
        if x.count(d) > target_count and d not in result:
            result.append(d)
    return result

print(appear4PlusTimes(arr))
