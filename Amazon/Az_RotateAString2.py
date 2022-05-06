""" Rotate a string ("this is a string" > "string this is a") """

input = "This is a string"
string_length = len(input)
arr = input.split()
l = len(arr[-1])  # len of the last element in array

def rotateAString(x):
    leftPart = x[string_length-l:string_length]  # string
    rigthPart = x[0:string_length-l]
    result = leftPart +" "+ rigthPart
    return result

print(rotateAString(input))
