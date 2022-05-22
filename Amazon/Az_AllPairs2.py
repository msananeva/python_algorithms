"""All Pairs > Lists > Cartesian Product"""

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

cartesian_product = [(a,b) for a in arr1 for b in arr2]

print(cartesian_product)
