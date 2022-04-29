""" Split the String
The split() method splits a string into a list.
separator	Optional. Specifies the separator to use when splitting the string.
By default any whitespace is a separator
"""

txt = "apple#banana#cherry#orange"

x = txt.split('#')
print(x)  # ['apple', 'banana', 'cherry', 'orange']

#____________________________________________________________

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements
x = txt.split("#", 1)
print(x)  # ['apple', 'banana#cherry#orange']
