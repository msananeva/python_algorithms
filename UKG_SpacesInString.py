""" Find if there are spaces in a string"""

test_str = "Hello World!"
print("The original string is : " + test_str)

# Using in operator check for spaces
res = " " in test_str
print(str(res))


print(test_str.isspace())  # checks if the string has ONLY spaces
