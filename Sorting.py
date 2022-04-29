""" Sorting """

# list.sort() changes the list

metals = ["Fe", "Cu", "Zn", "Au"]

metals.sort()  # Sort alphabetically by default

metals.sort(reverse=True)  # Sort in non-alphabetical order

print(metals)  # Sort alphabetically by default

"""
Sorting planets by size with the largest first. 
To do this we need a function to return the value to sort by. 
In this case we want a function that returns the second value of the tuple.
we can do it with the lambda expression. 
The input is a tuple of planet data. 
And the output is the second value.
Call the sort data and pass the size function as a key.
Return from the largest to smallest, specify reverse = True
by position of the element in the list of data
"""

planets = [
    ("Mercury", 2400, 5.43, 0.395),
    ("Earth", 6052, 5.24, 0.723),
    ("Mars", 3396, 3.93, 1.530)
    ]

size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
# planets.sort(key = density) #This will return the list from the less dense planet to more dense
print(planets)

""" How to create a sorted copy WITHOUT CHANGING THE LIST? 
And how to sort a tuple? 
Use builtins function sorted() """

metals = ["Fe", "Cu", "Zn", "Au"]

print(sorted(metals))


""" Tuples do NOT have a sort method, bc the data can not be changed.
But if you pass this to the sorted function, it returns the sorted LIST. """

data = (4, 6, 7, 2, 10)

print(sorted(data))  # Return sorted tuple as a list. Reverse = False by default

print(data)  # Return an initial tuple

print(sorted("Alphabetical", reverse=True))


# Return all chars in the string in non-alphabetical order
str = "Avocado"
print(sorted(str, reverse=False))
