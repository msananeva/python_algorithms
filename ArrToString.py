""" arr to str """

arr = ["This", "is", "a", "string"]

#The join method is used to combine the elements of a list into a single string, 
# with a specified separator between each element.
# NOTE: all elements must be strings

x = " ".join(arr)

print(x)

arr = ["This", "is", 1, "string"]
x = " ".join(str(item) for item in arr)
print(x)  # Output: This is 1 string